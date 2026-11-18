#!/usr/bin/env python3
"""Reproduce the household intent-to-treat DiD from the canonical notebook.

Primary specification (Analysis A1 in
``notebooks/store_performance_analysis_with_DiD.ipynb``):

    delta = post_spend - pre_spend            (56-day windows around Campaign 18)
    ATT   = mean(delta | treated) - mean(delta | clean controls)

Standard errors are HC1 for the two-parameter regression ``delta ~ treated``,
which is what the notebook reports. No notebook, no pandas, no statsmodels —
stdlib only, so it runs on any Python 3.9+.

The raw dunnhumby files are not committed (``datasets/*.csv`` is gitignored,
transaction_data.csv alone is ~140 MB):

    transaction_data.csv, campaign_desc.csv, campaign_table.csv

Usage
-----
    python scripts/did_estimate.py
    python scripts/did_estimate.py --data-dir /path/to/dunnhumby/csv
    python scripts/did_estimate.py --export-frame /tmp/did_frame.csv
    python scripts/did_estimate.py --from-frame /tmp/did_frame.csv
    python scripts/did_estimate.py --self-test

``--expect-uplift 2.84`` makes the script fail unless the reproduced estimate
matches the published headline within ``--tolerance`` percentage points.
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics
import sys
from pathlib import Path

# Same constants as the notebook's kernel-configuration cell.
PRE_START, PRE_END = 531, 586
POST_START, POST_END = 587, 642
CAMPAIGN_DID = 18
OUTLIER_QTY_MAX = 61335
OUTLIER_SALES_MAX = 631.8
OUTLIER_DISC_MIN = -100.0

FRAME_FIELDS = ["household_key", "pre", "post", "pre_trips", "treated", "is_control"]


def _rows(path: Path):
    with path.open(newline="") as handle:
        yield from csv.DictReader(handle)


def _float(row: dict, key: str) -> float:
    value = row.get(key) or 0
    try:
        return float(value)
    except ValueError:
        return 0.0


def _campaign_rows(data_dir: Path):
    """(campaign, household) pairs plus campaign windows, in one pass each."""
    desc = {
        int(row["CAMPAIGN"]): (int(row["START_DAY"]), int(row["END_DAY"]))
        for row in _rows(data_dir / "campaign_desc.csv")
    }
    assigned = [
        (int(row["CAMPAIGN"]), int(row["household_key"]))
        for row in _rows(data_dir / "campaign_table.csv")
    ]
    return desc, assigned


def build_frame(data_dir: Path) -> tuple[list[dict], int]:
    """Stream transaction_data.csv once; return household window rows + treated count."""
    desc, assigned = _campaign_rows(data_dir)

    overlapping = {
        campaign for campaign, (start, end) in desc.items()
        if start <= POST_END and end >= PRE_START
    }
    treated_hh = {household for campaign, household in assigned if campaign == CAMPAIGN_DID}
    contaminated_hh = {household for campaign, household in assigned if campaign in overlapping}

    pre: dict[int, float] = {}
    post: dict[int, float] = {}
    pre_days: dict[int, set[int]] = {}
    seen: set[int] = set()

    for row in _rows(data_dir / "transaction_data.csv"):
        quantity = _float(row, "QUANTITY")
        sales = _float(row, "SALES_VALUE")
        discount = _float(row, "RETAIL_DISC")
        # Notebook outlier caps: each boundary is a data error, not a transaction.
        if not (quantity < OUTLIER_QTY_MAX and quantity != 0
                and sales < OUTLIER_SALES_MAX and discount > OUTLIER_DISC_MIN):
            continue
        day = int(row["DAY"])
        if not (PRE_START <= day <= POST_END):
            continue
        household = int(row["household_key"])
        seen.add(household)
        if day <= PRE_END:
            pre[household] = pre.get(household, 0.0) + sales
            pre_days.setdefault(household, set()).add(day)
        else:
            post[household] = post.get(household, 0.0) + sales

    control_pool_hh = seen - contaminated_hh - treated_hh
    frame = [
        {
            "household_key": household,
            "pre": pre.get(household, 0.0),
            "post": post.get(household, 0.0),
            "pre_trips": len(pre_days.get(household, ())),
            "treated": int(household in treated_hh),
            "is_control": int(household in control_pool_hh),
        }
        for household in sorted(seen)
    ]
    return frame, len(treated_hh)


def estimate(frame: list[dict]) -> dict:
    """Difference-in-means ATT with HC1 standard errors (delta ~ treated)."""
    rows = [row for row in frame if row["treated"] or row["is_control"]]
    treated = [row["post"] - row["pre"] for row in rows if row["treated"]]
    control = [row["post"] - row["pre"] for row in rows if not row["treated"]]
    if len(treated) < 2 or len(control) < 2:
        raise ValueError("need at least two treated and two control households")

    beta = statistics.mean(treated) - statistics.mean(control)
    n1, n0 = len(treated), len(control)
    n, k = n1 + n0, 2
    variance = (statistics.variance(treated) / n1 + statistics.variance(control) / n0) * n / (n - k)
    se = math.sqrt(variance)
    t_stat = beta / se if se else float("inf")
    p_value = math.erfc(abs(t_stat) / math.sqrt(2))  # normal approximation; n is large
    pre_treated = [row["pre"] for row in rows if row["treated"]]

    return {
        "att": beta,
        "se": se,
        "p_value": p_value,
        "ci_low": beta - 1.96 * se,
        "ci_high": beta + 1.96 * se,
        "uplift_pct": 100.0 * beta / statistics.mean(pre_treated),
        "n_treated": n1,
        "n_control": n0,
        "pre_treated": statistics.mean(pre_treated),
        "post_treated": statistics.mean(row["post"] for row in rows if row["treated"]),
        "pre_control": statistics.mean(row["pre"] for row in rows if not row["treated"]),
        "post_control": statistics.mean(row["post"] for row in rows if not row["treated"]),
    }


def report(result: dict, assigned: int | None) -> None:
    print(f"n_treated={result['n_treated']:,}  n_control={result['n_control']:,}")
    print(
        "          pre     post\n"
        f"treated   {result['pre_treated']:7.2f} {result['post_treated']:8.2f}\n"
        f"control   {result['pre_control']:7.2f} {result['post_control']:8.2f}"
    )
    print(
        f"ATT = ${result['att']:+.2f}/household per 56d "
        f"(HC1 se ${result['se']:.2f}, 95% CI [{result['ci_low']:+.2f}, {result['ci_high']:+.2f}], "
        f"p={result['p_value']:.3f})"
    )
    print(f"uplift = {result['uplift_pct']:+.2f}% of treated pre-period spend")
    if assigned is not None:
        print(f"incremental revenue = ${result['att'] * assigned:,.0f} "
              f"across {assigned:,} assigned households")


def read_frame(path: Path) -> list[dict]:
    return [
        {key: (float(row[key]) if key in ("pre", "post") else int(float(row[key])))
         for key in FRAME_FIELDS}
        for row in _rows(path)
    ]


def write_frame(path: Path, frame: list[dict]) -> int:
    rows = [row for row in frame if row["treated"] or row["is_control"]]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FRAME_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def self_test() -> None:
    """Prove the estimator on a frame with a known ATT."""
    control = [{"household_key": i, "pre": 100.0, "post": 104.0, "pre_trips": 4,
                "treated": 0, "is_control": 1} for i in range(50)]
    treated = [{"household_key": 1000 + i, "pre": 200.0, "post": 209.0, "pre_trips": 6,
                "treated": 1, "is_control": 0} for i in range(50)]
    result = estimate(treated + control)
    assert abs(result["att"] - 5.0) < 1e-9, result["att"]
    assert abs(result["uplift_pct"] - 2.5) < 1e-9, result["uplift_pct"]
    assert result["se"] == 0.0, result["se"]

    # Non-degenerate control spread exercises the HC1 term.
    spread = [{"household_key": i, "pre": 100.0, "post": 100.0 + i, "pre_trips": 4,
               "treated": 0, "is_control": 1} for i in range(50)]
    result = estimate(treated + spread)
    assert result["se"] > 0 and result["ci_low"] < result["att"] < result["ci_high"]

    print("self-test PASS: ATT=+$5.00, uplift=+2.50%, HC1 SE > 0 on a spread frame")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--data-dir", type=Path,
                        help="directory holding transaction_data.csv, campaign_desc.csv, "
                             "campaign_table.csv (default: <project>/datasets)")
    parser.add_argument("--export-frame", type=Path, help="write the aggregated household frame and exit")
    parser.add_argument("--from-frame", type=Path, help="estimate from a previously exported frame (no raw data)")
    parser.add_argument("--self-test", action="store_true", help="run the synthetic estimator check and exit")
    parser.add_argument("--expect-uplift", type=float, help="fail unless the uplift matches this percentage")
    parser.add_argument("--tolerance", type=float, default=0.05, help="tolerance in percentage points (default 0.05)")
    args = parser.parse_args(argv)

    if args.self_test:
        self_test()
        return 0

    if args.from_frame:
        frame, assigned = read_frame(args.from_frame), None
    else:
        data_dir = args.data_dir or Path(__file__).resolve().parent.parent / "datasets"
        missing = [
            name for name in ("transaction_data.csv", "campaign_desc.csv", "campaign_table.csv")
            if not (data_dir / name).exists()
        ]
        if missing:
            print(
                f"missing {', '.join(missing)} in {data_dir} — "
                "the raw dunnhumby files are not committed (see datasets/README.md). "
                "Pass --data-dir, or use --export-frame/--from-frame once you have them.",
                file=sys.stderr,
            )
            return 2
        frame, assigned = build_frame(data_dir)

    if args.export_frame:
        print(f"wrote {write_frame(args.export_frame, frame):,} household rows to {args.export_frame}")
        return 0

    result = estimate(frame)
    report(result, assigned)

    if args.expect_uplift is not None:
        gap = abs(result["uplift_pct"] - args.expect_uplift)
        if gap > args.tolerance:
            print(f"MISMATCH: expected {args.expect_uplift:+.2f}% ± {args.tolerance}, "
                  f"got {result['uplift_pct']:+.2f}%", file=sys.stderr)
            return 1
        print(f"reproduces the published headline ({args.expect_uplift:+.2f}%) within {gap:.3f} pp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
