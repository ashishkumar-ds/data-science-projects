# app/

FastAPI service for the sales forecast model. Runs as `app.main:app`.

## Files
- `main.py` — API routes and inference logic
- `sales_forecast_model.pkl` — trained model (HistGradientBoostingRegressor)
- `daily_store_features.pkl` — feature store for lag/rolling inputs

## Endpoints
- `GET /health`
- `GET /stores`
- `POST /predict` — `{store_id, day, quantity?, baskets?}` → forecasted sales

Full schema at `/docs`.

## Note
Model requires same-day `quantity`/`baskets`; estimated automatically if omitted (see `quantity_was_estimated` in response).
