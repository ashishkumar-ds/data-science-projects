"""Offline tests for the Retail Sales Forecast API (in-process TestClient).

Runs against the real committed model artifacts (sales_forecast_model.pkl,
daily_store_features.pkl) - no network, no server. Run with: pytest -q
"""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from app.main import HISTORY, app  # noqa: E402

client = TestClient(app)

# A store with enough history for the 14-day lag/rolling requirements
STORE = int(HISTORY.groupby("STORE_ID").size().idxmax())
LAST_DAY = int(HISTORY[HISTORY.STORE_ID == STORE]["DAY"].max())


def test_root_lists_endpoints():
    body = client.get("/").json()
    assert body["version"] == "2.1.0"
    assert any("predict" in e for e in body["endpoints"])


def test_predict_within_history_returns_observed_lag_features():
    day = LAST_DAY  # a day with real history
    r = client.post("/predict", json={"store_id": STORE, "day": day})
    assert r.status_code == 200
    body = r.json()
    assert body["store_id"] == STORE
    assert body["days_forecasted_ahead"] == 0
    assert body["predicted_sales_value"] >= 0
    assert body["model_validation_mae"] > 0


def test_predict_iterates_forward_beyond_history():
    r = client.post("/predict", json={"store_id": STORE, "day": LAST_DAY + 7})
    assert r.status_code == 200
    body = r.json()
    assert body["days_forecasted_ahead"] == 7
    assert body["predicted_sales_value"] >= 0


def test_predict_rejects_too_far_ahead():
    r = client.post("/predict", json={"store_id": STORE, "day": LAST_DAY + 91})
    assert r.status_code == 400
    assert "90 days" in r.json()["detail"]


def test_predict_rejects_unknown_store():
    r = client.post("/predict", json={"store_id": 999999, "day": LAST_DAY})
    assert r.status_code == 400


def test_predict_rejects_insufficient_prior_history():
    first_day = int(HISTORY[HISTORY.STORE_ID == STORE]["DAY"].min())
    r = client.post("/predict", json={"store_id": STORE, "day": first_day})
    assert r.status_code == 400


def test_actuals_returns_only_observed_days_in_range():
    start = LAST_DAY - 100  # API caps ranges at 400 days
    r = client.get(f"/actuals/{STORE}", params={"start_day": start, "end_day": LAST_DAY})
    assert r.status_code == 200
    body = r.json()
    days = [row["day"] for row in body["observations"]]
    assert days == sorted(days)
    assert body["observation_count"] == len(days)
    assert all(row["sales_value"] >= 0 for row in body["observations"])


def test_actuals_rejects_bad_range():
    r = client.get(f"/actuals/{STORE}", params={"start_day": 10, "end_day": 5})
    assert r.status_code == 400


def test_stores_summarises_history():
    r = client.get("/stores")
    assert r.status_code == 200
    rows = r.json()
    sample = next(row for row in rows if row["store_id"] == STORE)
    assert sample["last_day"] == LAST_DAY
    assert sample["days_with_data"] > 0


@pytest.mark.parametrize("k", [3])
def test_controls_returns_matched_controls(k):
    r = client.get(
        f"/controls/{STORE}",
        params={"pre_start": 531, "pre_end": 586, "post_start": 587, "post_end": 642, "k": k},
    )
    assert r.status_code == 200
    body = r.json()
    assert len(body["matched_controls"]) == k
    assert "did_uplift_pct" in body["causal"]
