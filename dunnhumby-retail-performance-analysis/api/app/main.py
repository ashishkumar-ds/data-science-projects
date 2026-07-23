"""
Retail Sales Forecast API
===========================
Serves a store-level daily sales forecasting model
(scikit-learn HistGradientBoostingRegressor) as a REST API, for other
systems to call — e.g. an automation pipeline deciding campaign rollout.

MODELING NOTE: this model was trained with QUANTITY and BASKETS as
same-day features, so it is a same-day / nowcasting model, not a pure
N-days-ahead forecaster. If a caller doesn't know the target day's
transaction volume yet, the API substitutes the store's recent rolling
average and flags this in the response.
"""

from pathlib import Path
from typing import Optional

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

APP_DIR = Path(__file__).parent

app = FastAPI(
    title="Retail Sales Forecast API",
    description="Store-level daily sales forecasting model, served for production use.",
    version="1.0.0",
)

MODEL = joblib.load(APP_DIR / "sales_forecast_model.pkl")
HISTORY = (
    pd.read_pickle(APP_DIR / "daily_store_features.pkl")
    .sort_values(["STORE_ID", "DAY"])
    .reset_index(drop=True)
)
FEATURE_COLS = ["DOW", "WEEK", "QUANTITY", "BASKETS", "lag_1", "lag_7", "lag_14", "roll7_mean"]

# Validation metrics captured at training time
VALIDATION_MAE = 30.64
VALIDATION_WMAPE = 24.07


class PredictRequest(BaseModel):
    store_id: int = Field(..., description="Store ID to forecast for")
    day: int = Field(..., description="Day index to forecast (same DAY numbering as source dataset)")
    quantity: Optional[float] = Field(None, description="Expected units sold that day, if known. Estimated from recent history if omitted.")
    baskets: Optional[float] = Field(None, description="Expected number of baskets/transactions that day, if known. Estimated if omitted.")


class PredictResponse(BaseModel):
    store_id: int
    day: int
    predicted_sales_value: float
    quantity_used: float
    baskets_used: float
    quantity_was_estimated: bool
    baskets_was_estimated: bool
    features_used: dict
    model_validation_mae: float
    model_validation_wmape_pct: float


@app.get("/health")
def health():
    return {"status": "ok", "stores_available": int(HISTORY.STORE_ID.nunique())}


@app.get("/stores")
def list_stores():
    summary = HISTORY.groupby("STORE_ID")["DAY"].agg(["min", "max", "count"]).reset_index()
    summary.columns = ["store_id", "first_day", "last_day", "days_with_data"]
    return summary.to_dict(orient="records")


def _build_features(store_id: int, day: int, quantity: Optional[float], baskets: Optional[float]):
    store_hist = HISTORY[(HISTORY.STORE_ID == store_id) & (HISTORY.DAY < day)].sort_values("DAY")
    if len(store_hist) < 14:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Not enough history for store {store_id} before day {day} "
                f"(need at least 14 prior records with sales, found {len(store_hist)}). "
                f"Use GET /stores to check data availability for this store."
            ),
        )

    recent = store_hist.tail(14)
    lag_1 = store_hist.iloc[-1]["SALES_VALUE"]
    lag_7 = store_hist.iloc[-7]["SALES_VALUE"]
    lag_14 = store_hist.iloc[-14]["SALES_VALUE"]
    roll7_mean = store_hist.tail(7)["SALES_VALUE"].mean()

    quantity_estimated = quantity is None
    baskets_estimated = baskets is None
    quantity_val = quantity if quantity is not None else float(recent.tail(7)["QUANTITY"].mean())
    baskets_val = baskets if baskets is not None else float(recent.tail(7)["BASKETS"].mean())

    features = {
        "DOW": day % 7,
        "WEEK": (day - 1) // 7,
        "QUANTITY": quantity_val,
        "BASKETS": baskets_val,
        "lag_1": lag_1,
        "lag_7": lag_7,
        "lag_14": lag_14,
        "roll7_mean": roll7_mean,
    }
    return features, quantity_estimated, baskets_estimated


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    features, qty_est, bask_est = _build_features(req.store_id, req.day, req.quantity, req.baskets)
    X = pd.DataFrame([features])[FEATURE_COLS]
    pred = float(MODEL.predict(X)[0])

    return PredictResponse(
        store_id=req.store_id,
        day=req.day,
        predicted_sales_value=round(pred, 2),
        quantity_used=round(features["QUANTITY"], 2),
        baskets_used=round(features["BASKETS"], 2),
        quantity_was_estimated=qty_est,
        baskets_was_estimated=bask_est,
        features_used=features,
        model_validation_mae=VALIDATION_MAE,
        model_validation_wmape_pct=VALIDATION_WMAPE,
    )


@app.get("/")
def root():
    return {
        "message": "Retail Sales Forecast API",
        "docs": "/docs",
        "endpoints": ["/health", "/stores", "/predict (POST)"],
    }
