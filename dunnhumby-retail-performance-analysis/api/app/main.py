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
    description="Store-level daily sales forecasting model (LightGBM, Optuna-tuned), served for production use.",
    version="2.0.0",
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
        "endpoints": ["/health", "/stores", "/predict (POST)"],
    }
