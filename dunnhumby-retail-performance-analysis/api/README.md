# Retail Sales Forecast API

A production-ready REST API built with FastAPI for store-level daily sales forecasting.

---

## 1. Build the Docker Image

```bash
docker build -t retail-forecast-api .
```

---

## 2. Run Locally

```bash
docker run -p 8000:8000 retail-forecast-api
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 3. Smoke Test

### Health Check

```bash
curl http://127.0.0.1:8000/health
```

### Available Stores

```bash
curl http://127.0.0.1:8000/stores
```

### Prediction

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"store_id": 299, "day": 650}'
```

### Observed Sales (actuals) — for v4 feedback loop

```bash
curl "http://127.0.0.1:8000/actuals/317?start_day=594&end_day=650"
```

Returns `{store_id, start_day, end_day, observation_count, observations:[{day,date,sales_value}]}` — days without transactions are omitted, gaps are evidence not backfilled. Used by `POST /phase2/.../outcome?started_day=650`.

### Matched-Control DiD — for causal guardrail

```bash
curl "http://127.0.0.1:8000/controls/317?pre_start=531&pre_end=586&post_start=587&post_end=642&k=10"
```

Returns `{store_id, windows, matched_controls:[{store_id,distance}], causal:{did_uplift_pct,treated_change_pct,control_change_pct}, methodology:{matching,effect,caveat}}`. `did_uplift_pct` nets out the `+9.7%` market drift measured in the notebook; `v4` requires `did>=3% (CONFIRMED)` to scale.

---

## 4. Deploy (Render – Docker Environment)

1. Push this folder to a GitHub repository.
2. In the Render dashboard, select **New → Web Service** and connect the repository.
3. Choose **Docker** as the environment (Render automatically detects the `Dockerfile`; no build or start command is required).
4. Deploy the service to obtain a public URL such as:

```text
https://retail-forecast-api.onrender.com
```

---

## 5. Verify Production

```bash
curl https://<your-app>.onrender.com/health
```

---


## 6. Feedback & Causal Endpoints (v2.1)

| Endpoint | Use | Notes |
|---|---|---|
| `GET /actuals/{store_id}` | v4 replay outcome | Historical observed sales, 400-day window cap |
| `GET /controls/{store_id}` | v4 `scale_up_eligible` | k-NN on `log pre-sales + intra-pre trend`, `>=80%` coverage, `did_uplift_pct` |

---

## Production Readiness

- Add API authentication (API key or authorization header)
- Add structured logging for prediction requests (inputs, outputs, and timestamps) to support monitoring and auditing
- Model: **LightGBM (Optuna-tuned)** with **45–53% wMAPE** across validated pilot stores and a **30.1% pooled sales uplift** (95% CI: **+11.9% to +51.0%**) — *forecast uplift is optimistic; causal DiD in the notebook is `+2.84% ITT` (p0.10) / `-9.6%` store-level. v4 gates scale-up on `did>=3%` via `/controls`.*

---

## Project Structure

```text
retail_api/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI application
│   ├── sales_forecast_model.pkl     # Trained LightGBM (Optuna-tuned) model
│   └── daily_store_features.pkl     # Historical features for lag and rolling calculations
├── Dockerfile
├── requirements.txt
└── .dockerignore
```
