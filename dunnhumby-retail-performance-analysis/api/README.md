# Retail Sales Forecast API

A store-level daily sales forecasting model, served as a production **FastAPI** REST API.

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


## Production Readiness

- Add API authentication (API key or authorization header)
- Add structured logging for prediction requests (inputs, outputs, and timestamps) to support monitoring and auditing
- Model: **LightGBM (Optuna-tuned)** with **45–53% wMAPE** across validated pilot stores and a **30.1% pooled sales uplift** (95% CI: **+11.9% to +51.0%**)

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
