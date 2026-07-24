# Retail Sales Forecast API

A store-level daily sales forecast model, served as a production FAST API.

## Project structure
```
retail_api/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI app
│   ├── sales_forecast_model.pkl     # trained HistGradientBoostingRegressor
│   └── daily_store_features.pkl     # historical features (for lag/rolling lookups)
├── Dockerfile
├── requirements.txt
└── .dockerignore
```

## 1. Build the Docker image
```bash
docker build -t retail-forecast-api .
```

## 2. Run it locally
```bash
docker run -p 8000:8000 retail-forecast-api
```
Open http://127.0.0.1:8000/docs for the interactive API explorer.

## 3. Smoke test
```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/stores | head -c 300

curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"store_id": 32004, "day": 650}'
```

## 4. Deploy (Render, Docker environment)
1. Push this folder to a GitHub repo
2. Render dashboard → New → Web Service → connect the repo
3. Environment: **Docker** (Render auto-detects the Dockerfile — no build/start command needed)
4. Deploy → you get a URL like `retail-forecast-api.onrender.com`

## 5. Verify production
```bash
curl https://<your-app>.onrender.com/health
```

## Important modeling note
This model was trained with same-day `QUANTITY` and `BASKETS` as features — it's a
same-day / nowcasting model, not a pure N-days-ahead forecaster. If you don't pass
`quantity`/`baskets` in the request, the API substitutes the store's recent rolling
average and flags this in the response (`quantity_was_estimated`, `baskets_was_estimated`).

## Before connecting this to anything real
- Add an API key / auth header — this is currently open to anyone with the URL
- Add structured logging of every prediction (input, output, timestamp) for auditability
- Validation metrics from training: MAE $30.64, wMAPE 24.07% — substituted
  scikit-learn `HistGradientBoostingRegressor` for LightGBM/Optuna due to no
  package-install access during model development
