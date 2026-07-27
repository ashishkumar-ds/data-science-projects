# app/

FastAPI service for the sales forecast model. Runs as `app.main:app`.

## Files
- `main.py` — API routes and inference logic
- `sales_forecast_model.pkl` — trained LightGBM model (Optuna-tuned)
- `daily_store_features.pkl` — historical feature store for lag/rolling inputs

## Endpoints
- `GET /health`
- `GET /stores`
- `POST /predict` — `{store_id, day}` → forecasted sales

Full schema at `/docs`.

## Note
N-days-ahead forecaster using calendar features (day of week, month, weekend) and prior-day lag/rolling values. Requesting a day beyond stored history forecasts forward iteratively, one day at a time (max 90 days out).