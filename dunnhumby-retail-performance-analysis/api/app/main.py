"""
Retail Sales Forecast API
===========================
Serves the store-level daily sales forecasting model from
store_performance_analysis.ipynb (LightGBM, Optuna-tuned) as a REST API.

This is a genuine N-days-ahead forecaster: unlike the previous version of
this API, it does NOT require same-day QUANTITY/BASKETS as input. Features
are calendar-based (day of week, month, weekend flag) plus lag/rolling
features built entirely from prior days' sales - the same feature set used
in the notebook's forecast_iteratively() function. Predicting a day beyond
the stored history is done by iteratively forecasting forward one day at a
time, exactly as the notebook does for the Campaign 18 pilot validation.
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

APP_DIR = Path(__file__).parent

app = FastAPI(
    title="Retail Sales Forecast API",
    description="Store-level daily sales forecasting model (LightGBM, Optuna-tuned), served for production use. "
                "New in 2.1: GET /actuals/{store_id} (observed sales) and GET /controls/{store_id} (matched-control DiD) "
                "for the v4 feedback loop and causal guardrail.",
    version="2.1.0",
)

MODEL = joblib.load(APP_DIR / "sales_forecast_model.pkl")
HISTORY = (
    pd.read_pickle(APP_DIR / "daily_store_features.pkl")
    .sort_values(["STORE_ID", "DAY"])
    .reset_index(drop=True)
)
FEATURE_COLS = ["STORE_ID", "dow", "month", "is_weekend", "lag_7", "lag_14", "ma_7", "ma_14"]

# Validation metrics captured at training time (held-out chronological split)
VALIDATION_MAE = 65.68
VALIDATION_WMAPE = 51.29


class PredictRequest(BaseModel):
    store_id: int = Field(..., description="Store ID to forecast for")
    day: int = Field(..., description="Day index to forecast (same DAY numbering as source dataset)")


class PredictResponse(BaseModel):
    store_id: int
    day: int
    predicted_sales_value: float
    days_forecasted_ahead: int
    model_validation_mae: float
    model_validation_wmape_pct: float


def _day_to_date(day: int) -> pd.Timestamp:
    year = 2017 if day < 366 else 2018
    day_num = day - 365 if day > 365 else day
    return pd.Timestamp(year=year, month=1, day=1) + pd.Timedelta(days=day_num - 1)


def _row_features(date: pd.Timestamp, lag_7: float, lag_14: float, ma_7: float, ma_14: float, store_id: int) -> dict:
    return {
        "STORE_ID": store_id,
        "dow": date.dayofweek,
        "month": date.month,
        "is_weekend": int(date.dayofweek >= 5),
        "lag_7": lag_7,
        "lag_14": lag_14,
        "ma_7": ma_7,
        "ma_14": ma_14,
    }


@app.get("/actuals/{store_id}")
def get_actuals(store_id: int, start_day: int, end_day: int):
    """Observed daily sales for a store, from the historical feature store.

    This is REAL observed transaction data (the same history the forecaster
    trains on), not a prediction. Consumers (e.g. Project 3's outcome
    evaluator) use it to measure what actually happened during an
    intervention window versus what was forecast - the observed arm of the
    outcome feedback loop.

    Day numbering matches /predict (same DAY indices as the source dataset).
    Days in range without observed transactions are omitted, so callers must
    treat coverage as evidence, not assume completeness.
    """
    if start_day > end_day:
        raise HTTPException(status_code=400, detail="start_day must not exceed end_day")
    if end_day - start_day > 400:
        raise HTTPException(status_code=400, detail="day range must not exceed 400 days")
    store_hist = HISTORY[HISTORY.STORE_ID == store_id]
    if store_hist.empty:
        raise HTTPException(status_code=404, detail=f"Unknown store {store_id}. Use GET /stores.")
    window = store_hist[(store_hist.DAY >= start_day) & (store_hist.DAY <= end_day)]
    observations = [
        {"day": int(row.DAY), "date": _day_to_date(int(row.DAY)).date().isoformat(), "sales_value": round(float(row.SALES_VALUE), 2)}
        for row in window.itertuples()
    ]
    return {
        "store_id": store_id,
        "start_day": start_day,
        "end_day": end_day,
        "range_start_date": _day_to_date(start_day).date().isoformat(),
        "range_end_date": _day_to_date(end_day).date().isoformat(),
        "observation_count": len(observations),
        "observations": observations,
    }


@app.get("/controls/{store_id}")
def get_matched_controls(
    store_id: int,
    pre_start: int = 531,
    pre_end: int = 586,
    post_start: int = 587,
    post_end: int = 642,
    k: int = 10,
    pool: str = "all",
):
    """Matched-control comparison for causal (DiD) validation.

    Productionized from the DiD notebook's Analysis B (store-level): a treated
    store is matched against untreated stores on pre-window sales level and
    intra-pre trend (z-scored, Euclidean k-NN), then the causal effect is the
    difference between the treated and control pre->post sales change. This
    nets out market-wide drift that inflates single-series (forecast or
    own-baseline) lift estimates - the notebook measured +9.7% market drift
    during Campaign 18, which is exactly what raw lift wrongly credits to the
    intervention.

    Consumers (Project 3's causal guardrail) must treat the returned
    did_uplift_pct - not raw lift - as the scale-up decision input.

    ``pool`` selects the control universe: ``"all"`` (default, every other
    store with coverage — byte-identical to previous behavior) or
    ``"underperforming"`` (bottom-tercile pre-window mean sales, so treated
    stores selected for being low are compared against stores that share
    the same selection mechanism and its regression-to-the-mean bounce).
    """
    if pool not in ("all", "underperforming"):
        raise HTTPException(
            status_code=400, detail="pool must be 'all' or 'underperforming'")
    pool_name: str = pool
    if pre_start >= pre_end or post_start > post_end or pre_end >= post_start:
        raise HTTPException(
            status_code=400,
            detail="windows must satisfy pre_start < pre_end < post_start <= post_end",
        )
    if post_end - pre_start > 400:
        raise HTTPException(status_code=400, detail="window span must not exceed 400 days")
    if isinstance(k, bool) or k < 1 or k > 25:
        raise HTTPException(status_code=400, detail="k must be between 1 and 25")

    treated_hist = HISTORY[HISTORY.STORE_ID == store_id]
    if treated_hist.empty:
        raise HTTPException(status_code=404, detail=f"Unknown store {store_id}. Use GET /stores.")
    span = post_end - pre_start + 1

    def _features(df: pd.DataFrame) -> tuple[float, float] | None:
        """(log pre-sales level, intra-pre trend) for one store, or None if
        the store lacks the notebook's >=80% day coverage over the window."""
        days = df[(df.DAY >= pre_start) & (df.DAY <= post_end)]
        if days.DAY.nunique() / span < 0.8:
            return None
        pre = days[days.DAY <= pre_end].SALES_VALUE
        mid = pre_start + (pre_end - pre_start) // 2
        early = days[(days.DAY <= pre_end) & (days.DAY <= mid)].SALES_VALUE
        late = days[(days.DAY <= pre_end) & (days.DAY > mid)].SALES_VALUE
        if len(pre) == 0 or len(early) == 0 or len(late) == 0:
            return None
        return float(np.log1p(pre.mean())), float(late.mean() - early.mean())

    treated_feat = _features(treated_hist)
    if treated_feat is None:
        raise HTTPException(
            status_code=422,
            detail=f"Store {store_id} lacks >=80% day coverage over days {pre_start}-{post_end}; "
                   "a causal comparison is not computable.",
        )

    # Control pool: every other store with sufficient coverage (untreated by
    # construction - this API serves observed history, not campaign assignment).
    pool_feats: dict[int, tuple[float, float]] = {}
    for sid, grp in HISTORY.groupby("STORE_ID"):
        if int(sid) == store_id:
            continue
        feat = _features(grp)
        if feat is not None:
            pool_feats[int(sid)] = feat
    if not pool_feats:
        raise HTTPException(status_code=422, detail="no eligible control stores in the window")
    pool_rule = "all untreated stores with >=80% day coverage"
    if pool == "underperforming":
        # Regression-to-the-mean guard: treated stores were selected for
        # being low, and low stores bounce back on their own. Restrict the
        # pool to the bottom tercile of pre-window mean sales so the bounce
        # cancels out in the treated-minus-control difference.
        pre_means = {}
        for sid in pool_feats:
            days = HISTORY[(HISTORY.STORE_ID == sid)
                           & (HISTORY.DAY >= pre_start) & (HISTORY.DAY <= pre_end)]
            if len(days):
                pre_means[sid] = float(days.SALES_VALUE.mean())
        if not pre_means:
            raise HTTPException(status_code=422, detail="no pool sales means computable")
        cutoff = float(np.quantile(list(pre_means.values()), 1.0 / 3.0))
        pool_feats = {sid: feat for sid, feat in pool_feats.items()
                      if pre_means.get(sid, float("inf")) <= cutoff}
        if not pool_feats:
            raise HTTPException(status_code=422, detail="underperforming pool is empty")
        pool_rule = (f"bottom-tercile pre-window mean sales (cutoff "
                     f"{cutoff:.2f} over {len(pre_means)} covered stores)")
    pool: dict[int, tuple[float, float]] = pool_feats

    # Z-score features across pool + treated, then deterministic Euclidean
    # k-NN (numpy only; mirrors the notebook's NN on scaled features).
    all_ids = sorted(pool) + [store_id]
    X = np.array([pool[s] if s != store_id else treated_feat for s in all_ids])
    mu, sigma = X.mean(axis=0), X.std(axis=0)
    Xz = (X - mu) / np.where(sigma == 0, 1.0, sigma)
    dists = np.sqrt(((Xz[-1] - Xz[:-1]) ** 2).sum(axis=1))
    order = np.argsort(dists, kind="stable")[: min(k, len(pool))]
    control_ids = sorted(int(all_ids[i]) for i in order)

    def _window_mean(sid: int, start: int, end: int) -> float | None:
        days = HISTORY[(HISTORY.STORE_ID == sid) & (HISTORY.DAY >= start) & (HISTORY.DAY <= end)]
        return float(days.SALES_VALUE.mean()) if len(days) else None

    def _pct(pre_v: float, post_v: float) -> float:
        return (post_v / pre_v - 1) * 100 if pre_v > 0 else 0.0

    treated_pre = _window_mean(store_id, pre_start, pre_end)
    treated_post = _window_mean(store_id, post_start, post_end)
    ctrl_pre = [m for m in (_window_mean(s, pre_start, pre_end) for s in control_ids) if m is not None]
    ctrl_post = [m for m in (_window_mean(s, post_start, post_end) for s in control_ids) if m is not None]
    treated_change = _pct(treated_pre, treated_post) if treated_pre and treated_post else None
    control_change = (
        _pct(float(np.mean(ctrl_pre)), float(np.mean(ctrl_post))) if ctrl_pre and ctrl_post else None
    )
    did = (
        round(treated_change - control_change, 2)
        if treated_change is not None and control_change is not None
        else None
    )

    # Placebo check (report-only): same DiD machinery on the pre-window
    # split in half, where no intervention happened — a non-zero placebo
    # warns that treated and controls were already diverging.
    mid = pre_start + (pre_end - pre_start) // 2
    treated_early = _window_mean(store_id, pre_start, mid)
    treated_late = _window_mean(store_id, mid + 1, pre_end)
    ctrl_early = [m for m in (_window_mean(s, pre_start, mid) for s in control_ids)
                  if m is not None]
    ctrl_late = [m for m in (_window_mean(s, mid + 1, pre_end) for s in control_ids)
                 if m is not None]
    placebo_did = None
    if treated_early and treated_late and ctrl_early and ctrl_late:
        placebo_did = round(
            _pct(treated_early, treated_late)
            - _pct(float(np.mean(ctrl_early)), float(np.mean(ctrl_late))), 2)

    # Pre-trend divergence: treated intra-pre trend vs mean control trend
    # (both already computed as matching features). Large gaps weaken the
    # parallel-trends assumption the DiD rests on.
    control_trends = [pool[sid][1] for sid in control_ids]
    trend_divergence = (
        round(abs(float(treated_feat[1]) - float(np.mean(control_trends))), 2)
        if control_trends and treated_feat[1] is not None else None)

    # Uncertainty from control variation (report-only): per-control
    # pre->post change pcts give a standard error for the control mean
    # change; the 95% interval is normal-approx (z=1.96, noted as
    # approximate for small k). MDE = smallest |effect| clearing that bar.
    paired_changes = []
    for sid in control_ids:
        pre_mean = _window_mean(sid, pre_start, pre_end)
        post_mean = _window_mean(sid, post_start, post_end)
        if pre_mean and post_mean:
            paired_changes.append(_pct(pre_mean, post_mean))
    did_ci95: list[float] | None = None
    mde_pct: float | None = None
    if did is not None and len(paired_changes) >= 2:
        se = float(np.std(paired_changes, ddof=1)) / float(np.sqrt(len(paired_changes)))
        half_width = round(1.96 * se, 2)
        did_ci95 = [round(did - half_width, 2), round(did + half_width, 2)]
        mde_pct = half_width

    return {
        "store_id": store_id,
        "windows": {"pre_start": pre_start, "pre_end": pre_end,
                    "post_start": post_start, "post_end": post_end},
        "pool": pool_name,
        "matched_controls": [
            {"store_id": sid, "distance": round(float(dists[all_ids.index(sid)]), 4),
             "pre_log_mean_sales": round(float(pool[sid][0]), 4),
             "pre_trend": round(float(pool[sid][1]), 2)}
            for sid in control_ids
        ],
        "causal": {
            "treated_pre_daily_mean": round(treated_pre, 2) if treated_pre else None,
            "treated_post_daily_mean": round(treated_post, 2) if treated_post else None,
            "control_pre_daily_mean": round(float(np.mean(ctrl_pre)), 2) if ctrl_pre else None,
            "control_post_daily_mean": round(float(np.mean(ctrl_post)), 2) if ctrl_post else None,
            "treated_change_pct": round(treated_change, 2) if treated_change is not None else None,
            "control_change_pct": round(control_change, 2) if control_change is not None else None,
            "did_uplift_pct": did,
            "did_ci95": did_ci95,
            "mde_pct": mde_pct,
            "placebo_did_pct": placebo_did,
            "pre_trend_divergence": trend_divergence,
        },
        "methodology": {
            "matching": f"k={min(k, len(pool))} nearest neighbors on z-scored "
                        "[log pre-sales level, intra-pre trend] from a pool of "
                        f"{len(pool)} stores with >=80% day coverage "
                        f"({pool_rule})",
            "effect": "DiD = treated pre->post change - pooled matched-control pre->post change (%)",
            "uncertainty": "did_ci95/mde_pct from control-group variation "
                           "(normal-approx z=1.96, approximate for small k); "
                           "placebo_did_pct reruns the DiD on the pre-window "
                           "split in half (expect ~0); pre_trend_divergence "
                           "flags parallel-trends risk. All report-only: the "
                           "scale-up rule still keys on did_uplift_pct.",
            "caveat": "observational DiD, not a randomized experiment; "
                      "treated-vs-control, unlike own-baseline lift, nets out market drift",
        },
    }


@app.get("/health")
def health():
    return {"status": "ok", "stores_available": int(HISTORY.STORE_ID.nunique())}


@app.get("/stores")
def list_stores():
    summary = HISTORY.groupby("STORE_ID")["DAY"].agg(["min", "max", "count"]).reset_index()
    summary.columns = ["store_id", "first_day", "last_day", "days_with_data"]
    return summary.to_dict(orient="records")


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    store_hist = HISTORY[HISTORY.STORE_ID == req.store_id].sort_values("DAY")
    if len(store_hist) < 14:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Not enough history for store {req.store_id} "
                f"(need at least 14 days, found {len(store_hist)}). "
                f"Use GET /stores to check data availability for this store."
            ),
        )

    last_day = int(store_hist["DAY"].max())
    if req.day <= last_day:
        # Target day is within known history: pull real lag/rolling values directly
        prior = store_hist[store_hist.DAY < req.day]
        if len(prior) < 14:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough prior history before day {req.day} for store {req.store_id}.",
            )
        date = _day_to_date(req.day)
        lag_7 = prior.iloc[-7]["SALES_VALUE"]
        lag_14 = prior.iloc[-14]["SALES_VALUE"]
        ma_7 = prior.tail(7)["SALES_VALUE"].mean()
        ma_14 = prior.tail(14)["SALES_VALUE"].mean()
        features = _row_features(date, lag_7, lag_14, ma_7, ma_14, req.store_id)
        pred = float(MODEL.predict(pd.DataFrame([features])[FEATURE_COLS])[0])
        days_ahead = 0
    else:
        # Target day is beyond known history: forecast forward one day at a
        # time, feeding each prediction back in as history (same approach as
        # the notebook's forecast_iteratively()).
        hist = store_hist[["DAY", "SALES_VALUE"]].copy()
        days_ahead = req.day - last_day
        if days_ahead > 90:
            raise HTTPException(
                status_code=400,
                detail=f"Requested day is {days_ahead} days beyond available history; "
                        f"iterative forecasts beyond 90 days are not supported.",
            )
        pred = None
        for d in range(last_day + 1, req.day + 1):
            date = _day_to_date(d)
            lag_7 = hist.iloc[-7]["SALES_VALUE"]
            lag_14 = hist.iloc[-14]["SALES_VALUE"]
            ma_7 = hist.tail(7)["SALES_VALUE"].mean()
            ma_14 = hist.tail(14)["SALES_VALUE"].mean()
            features = _row_features(date, lag_7, lag_14, ma_7, ma_14, req.store_id)
            pred = float(MODEL.predict(pd.DataFrame([features])[FEATURE_COLS])[0])
            hist = pd.concat([hist, pd.DataFrame([{"DAY": d, "SALES_VALUE": pred}])], ignore_index=True)

    return PredictResponse(
        store_id=req.store_id,
        day=req.day,
        predicted_sales_value=round(pred, 2),
        days_forecasted_ahead=days_ahead,
        model_validation_mae=VALIDATION_MAE,
        model_validation_wmape_pct=VALIDATION_WMAPE,
    )


@app.get("/")
def root():
    return {
        "message": "Retail Sales Forecast API",
        "docs": "/docs",
        "version": "2.1.0",
        "endpoints": [
            "/health",
            "/stores",
            "/predict (POST)",
            "/actuals/{store_id} (GET, query: start_day, end_day)",
            "/controls/{store_id} (GET, query: pre_start, pre_end, post_start, post_end, k, pool)",
        ],
    }
