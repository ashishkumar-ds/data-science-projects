
# Dunnhumby Retail Store Performance Analysis – Notebooks

This folder contains notebooks that walk through the end-to-end dunnhumby analytics workflow from data cleaning and exploratory analysis to customer segmentation, campaign uplift modeling, forecasting, and business impact evaluation.

---

## Data Cleaning Notebook  
**File:** notebooks/data_cleaning.ipynb

### Objective  
Transform raw multi-source retail transaction data into a unified, validated, and analysis-ready dataset suitable for modeling and downstream analytics.

---

### 1. Data Understanding

| Data Source       | Rows       | Key Fields                                                |
|-------------------|------------|-----------------------------------------------------------|
| Transaction       | 2,595,914  | household_key, basket_id, product_id, quantity, sales_value, coupon_disc, day |
| Product           | 23,539     | department, brand, commodity, sub_commodity               |
| Household         | 103,200    | age_bracket, income_bracket, household_size               |
| Campaign_desc     | 30         | campaign_id, description, start_day, end_day              |
| Coupons           | 1,310,318  | campaign_id, household_key, product_id                    |

---

### 2. Data Preparation

| QC Gate                     | Rows Removed | % of Raw |
|-----------------------------|--------------|----------|
| Zero quantity               | 7,266        | 0.28%    |
| Coupon discount > sales value  | 6,206        | 0.24%    |
| Extreme outliers            | 10           | 0.00%    |
| **TOTAL REMOVED**           | **13,472**   | **0.52%**|

---

### 3. Feature Engineering

| Feature             | Definition                                | Business Role                  |
|---------------------|-------------------------------------------|--------------------------------|
| DATE              | Julian → calendar date                    | time-series index              |
| DAY_CATEGORY      | weekday / weekend                         | roster optimisation            |
| TIME_CATEGORY     | Day (06:00–17:59) / Night (18:00–05:59)               | store-hour decisions           |
| TIME_OF_DAY_CATEGORY    | morning / afternoon / evening / night     | promo timing                   |
| cust_purchase_value| net spend (sales_value + coupon_disc)    | LTV modelling                  |
| sales_lag_7       | sales 7 days ago                          | auto-regressive signal         |
| sales_ma_7        | 7-day moving average                      | trend smoothing                |


---

## Main Analysis Notebook  
**File:** notebooks/store_performance_analysis.ipynb

### Objective  
Identify performance drivers, segment customers by value, and quantify campaign uplift to generate recommendations for improving underperforming stores.

---

### 4. Exploratory Data Analysis

#### 4.1 Store Concentration (Pareto)

| Category              | Store Count | % of Total | Sales Contribution |
|-----------------------|-------------|------------|---------------------|
| Performing (Top 12%)  | 71          | 12%        | 80%                 |
| Underperforming       | 511         | 88%        | 20%                 |
| **Total**             | **582**     | **100%**   | **100%**            |

**Key Insight:**  
Top 12% of stores generate 80% of total sales, confirming a strong Pareto dynamic and justifying focused intervention on the long tail.

---

#### 4.2 Customer Traffic Patterns

| Dimension    | Level     | Footfall Share |
|--------------|-----------|----------------|
| Week-part    | weekday   | 65%            |
|              | weekend   | 35%            |
| Time-of-day  | **afternoon (12:00–18:00)** | **27%**    |
|              | evening (19:00–24:00)       | 25%            |
|              | morning (06:00–11:00)       | 24%            |
|              | night (00:00–05:00)         | 24%            |

**Key Insight:**  
Afternoon (12:00–18:00) is the peak engagement window for campaign delivery.

---

### 5. Campaign Uplift

| Campaign | Cust. CR | Coupon CR | Gross ROI | Sales Share | Incremental |
|----------|----------|-----------|-----------|-------------|-------------|
| 15       | 0.8%     | 4.8%      | 134%      | 13%         | $1.1M       |
| 16       | 4.4%     | 8.7%      | 272%      | 17%         | $2.0M       |
| 17       | 1.8%     | 5.0%      | 199%      | 22%         | $2.6M       |
| **18**   | **13.0%**| **9.1%**  | **411.4%**| **47%**     | **$5.5M**   |

> Net ROI for Campaign 18 = **278.7%** (after deducting 75% COGS and $1,500 campaign cost).

**Key Insight:**  
Campaign 18 drives the highest revenue share and ROI, making it the strongest candidate for scaling to underperforming stores.

---

### 6. Customer Segmentation (RFM)

| Segment   | % Customers | % Revenue | Avg Monetary | Campaign-18 Redemption |
|-----------|-------------|-----------|--------------|------------------------|
| **Best**      | **20.2%**       | **41%**       | **$1,246**       | **38%**                    |
| Loyal     | 20.3%       | 29%       | $682         | 32%                    |
| Promising | 21.0%       | 19%       | $413         | 18%                    |
| At-Risk   | 19.6%       | 10%       | $199         | 12%                    |
| Lost      | 18.8%       | 2%        | $75          | 0%                     |

**Key Insight:**  
Best Customers (20.2% of base) drive 41% of revenue and 38% of redemptions, the highest-value segment for retention and targeting.

---

### 7. Predictive Modelling — Sales Forecast

**Why Stores #299, #317, #448?**  
Selected as the ideal pilot stores among underperforming stores: Bottom ~15% by sales, 37/34/28 Best Customers respectively (highest three in cohort), and full Campaign 18 exposure with 480+ days of clean daily sales each.

| 
instruct me clearly

Yes. What you've built is a REST API implemented with FastAPI.

Here's why.

REST API
REST (Representational State Transfer) is an architectural style. A service is considered RESTful when it exposes resources through HTTP methods like:

HTTP Method	Your Endpoint	Purpose
GET	/health	Check service status
GET	/stores	Retrieve available store information
POST	/predict	Create a prediction from input data
Your API accepts JSON requests and returns JSON responses over HTTP, which is exactly how REST APIs commonly work.

Example:

Request

POST /predict
Content-Type: application/json

{
  "store_id": 299,
  "day": 650
}
Response

{
  "store_id": 299,
  "day": 650,
  "predicted_sales_value": 3021.87,
  ...
}
That's a REST endpoint.

Is FastAPI the right choice?
Absolutely.

FastAPI is one of the most popular frameworks for deploying machine learning models because it provides:

High performance (built on Starlette and Uvicorn)

Automatic request validation with Pydantic

Automatic interactive documentation (/docs)

Easy Docker deployment

Easy integration with cloud platforms like Render, Azure, AWS, or GCP

Many production ML services use FastAPI.

Your architecture
Client
(Postman / Swagger / n8n / Web App)

          │
          ▼

    FastAPI REST API
      (/predict)

          │
          ▼

Feature Engineering
(lag features, rolling averages)

          │
          ▼

HistGradientBoostingRegressor
(.pkl model)

          │
          ▼

Prediction (JSON)
This is a standard deployment architecture for an ML inference service.

How to describe it on GitHub
Instead of saying:

Built a FastAPI project

Say:

Deployed a machine learning model as a production-ready REST API using FastAPI and Docker.

Or:

Served a store-level sales forecasting model through a RESTful FastAPI service with interactive OpenAPI documentation and Docker-based deployment.

These descriptions communicate both the deployment technology and the API design.

Is this enough for MLOps?
It's a good start. Your project already includes:

✅ Trained ML model

✅ Saved model (.pkl)

✅ FastAPI inference service

✅ REST API endpoints

✅ Docker container

✅ Cloud deployment (Render)

✅ Interactive API documentation

To make it even stronger, you could add:

API authentication (API key or OAuth)

Request and prediction logging

Model versioning

Monitoring (latency, request counts, errors)

CI/CD with GitHub Actions

Automated tests for API endpoints

Those additions would move it closer to a production-grade MLOps deployment.


why i cant use only fast api?

You can use only FastAPI.

Docker is not required. It's simply a deployment tool.

Here's the difference:

Option 1: FastAPI only ✅
Run locally:

uvicorn app.main:app --host 0.0.0.0 --port 8000
Your API is live.

Architecture:

Client
   │
   ▼
FastAPI
   │
   ▼
ML Model (.pkl)
This is perfectly valid.

Option 2: FastAPI + Docker (what you currently have)
Docker packages:

Python

FastAPI

Dependencies

Model files

Your code

into one portable container.

Architecture:

Client
   │
   ▼
Docker Container
   │
   ▼
FastAPI
   │
   ▼
ML Model
Docker doesn't replace FastAPI—it packages it.

Why use Docker?
Imagine your project runs on your laptop because you have:

Python 3.12

pandas

joblib

scikit-learn

Now you deploy to another machine that has:

Python 3.10

Different pandas version

Missing scikit-learn

Your app may fail.

Docker ensures every environment is identical.

On Render
Render supports two ways to deploy FastAPI.

Method 1: Native Python (no Docker)
Repository:

api/
    app/
    requirements.txt
Render settings:

Build Command

pip install -r requirements.txt
Start Command

uvicorn app.main:app --host 0.0.0.0 --port $PORT
No Dockerfile needed.

Method 2: Docker
Repository:

api/
    Dockerfile
    requirements.txt
    app/
Render simply runs:

docker build
docker run
No build/start commands needed.

Which is better for your portfolio?
FastAPI only
Pros:

Simpler

Easier to understand

Faster to develop

Good for:

Small ML projects

Student portfolios

Interview demos

FastAPI + Docker
Pros:

Matches industry deployment practices

Environment consistency

Easy deployment across cloud platforms

Demonstrates familiarity with containerization

Good for:

Production-style portfolios

MLOps-focused roles

Backend/ML engineering positions

My recommendation for your project
Since you're targeting Data Scientist/Data Analyst roles and want to show you can deploy models, keep both:

FastAPI shows you can build and expose an ML inference service.

Docker shows you know how to package and deploy it consistently.

A good way to describe it in your README is:

Built a REST API using FastAPI to serve a store-level sales forecasting model, then containerized the service with Docker and deployed it on Render.

This accurately reflects what you've built and highlights both the API and deployment aspects.


Today 6:27 PM
Convert this into GitHub readme format.
[# Dunnhumby Retail Store Performance Analysis – Notebooks

This folder contains notebooks that walk through the end-to-end dunnhumby analytics workflow from data cleaning and exploratory analysis to customer segmentation, campaign uplift modeling, forecasting, and business impact evaluation.

---

## Data Cleaning Notebook  
**File:** notebooks/data_cleaning.ipynb

### Objective  
Transform raw multi-source retail transaction data into a unified, validated, and analysis-ready dataset suitable for modeling and downstream analytics.

---

### 1. Data Understanding

| Data Source       | Rows       | Key Fields                                                |
|-------------------|------------|-----------------------------------------------------------|
| Transaction       | 2,595,914  | household_key, basket_id, product_id, quantity, sales_value, coupon_disc, day |
| Product           | 23,539     | department, brand, commodity, sub_commodity               |
| Household         | 103,200    | age_bracket, income_bracket, household_size               |
| Campaign_desc     | 30         | campaign_id, description, start_day, end_day              |
| Coupons           | 1,310,318  | campaign_id, household_key, product_id                    |

---

### 2. Data Preparation

| QC Gate                     | Rows Removed | % of Raw |
|-----------------------------|--------------|----------|
| Zero quantity               | 7,266        | 0.28%    |
| Coupon discount > sales value  | 6,206        | 0.24%    |
| Extreme outliers            | 10           | 0.00%    |
| **TOTAL REMOVED**           | **13,472**   | **0.52%**|

---

### 3. Feature Engineering

| Feature             | Definition                                | Business Role                  |
|---------------------|-------------------------------------------|--------------------------------|
| DATE              | Julian → calendar date                    | time-series index              |
| DAY_CATEGORY      | weekday / weekend                         | roster optimisation            |
| TIME_CATEGORY     | Day (06:00–17:59) / Night (18:00–05:59)               | store-hour decisions           |
| TIME_OF_DAY_CATEGORY    | morning / afternoon / evening / night     | promo timing                   |
| cust_purchase_value| net spend (sales_value + coupon_disc)    | LTV modelling                  |
| sales_lag_7       | sales 7 days ago                          | auto-regressive signal         |
| sales_ma_7        | 7-day moving average                      | trend smoothing                |

---

## Main Analysis Notebook  
**File:** notebooks/store_performance_analysis.ipynb

### Objective  
Identify performance drivers, segment customers by value, and quantify campaign uplift to generate recommendations for improving underperforming stores.

---

### 4. Exploratory Data Analysis

#### 4.1 Store Concentration (Pareto)

| Category              | Store Count | % of Total | Sales Contribution |
|-----------------------|-------------|------------|---------------------|
| Performing (Top 12%)  | 71          | 12%        | 80%                 |
| Underperforming       | 511         | 88%        | 20%                 |
| **Total**             | **582**     | **100%**   | **100%**            |

**Key Insight:**  
Top 12% of stores generate 80% of total sales, confirming a strong Pareto dynamic and justifying focused intervention on the long tail.

---

#### 4.2 Customer Traffic Patterns

| Dimension    | Level     | Footfall Share |
|--------------|-----------|----------------|
| Week-part    | weekday   | 65%            |
|              | weekend   | 35%            |
| Time-of-day  | **afternoon (12:00–18:00)** | **27%**    |
|              | evening (19:00–24:00)       | 25%            |
|              | morning (06:00–11:00)       | 24%            |
|              | night (00:00–05:00)         | 24%            |

**Key Insight:**  
Afternoon (12:00–18:00) is the peak engagement window for campaign delivery.

---

### 5. Campaign Uplift

| Campaign | Cust. CR | Coupon CR | Gross ROI | Sales Share | Incremental |
|----------|----------|-----------|-----------|-------------|-------------|
| 15       | 0.8%     | 4.8%      | 134%      | 13%         | $1.1M       |
| 16       | 4.4%     | 8.7%      | 272%      | 17%         | $2.0M       |
| 17       | 1.8%     | 5.0%      | 199%      | 22%         | $2.6M       |
| **18**   | **13.0%**| **9.1%**  | **411.4%**| **47%**     | **$5.5M**   |

> Net ROI for Campaign 18 = **278.7%** (after deducting 75% COGS and $1,500 campaign cost).

**Key Insight:**  
Campaign 18 drives the highest revenue share and ROI, making it the strongest candidate for scaling to underperforming stores.

---

### 6. Customer Segmentation (RFM)

| Segment   | % Customers | % Revenue | Avg Monetary | Campaign-18 Redemption |
|-----------|-------------|-----------|--------------|------------------------|
| **Best**      | **20.2%**       | **41%**       | **$1,246**       | **38%**                    |
| Loyal     | 20.3%       | 29%       | $682         | 32%                    |
| Promising | 21.0%       | 19%       | $413         | 18%                    |
| At-Risk   | 19.6%       | 10%       | $199         | 12%                    |
| Lost      | 18.8%       | 2%        | $75          | 0%                     |

**Key Insight:**  
Best Customers (20.2% of base) drive 41% of revenue and 38% of redemptions, the highest-value segment for retention and targeting.

---

### 7. Predictive Modelling — Sales Forecast

**Why Stores #299, #317, #448?**  
Selected as the ideal pilot stores among underperforming stores: Bottom ~15% by sales, 37/34/28 Best Customers respectively (highest three in cohort), and full Campaign 18 exposure with 480+ days of clean daily sales each.

| Store | wMAPE   | Actual Sales | Counterfactual | Uplift |
|-------|---------|--------------|-----------------|--------|
| 299   | 52.9%   | $2,977       | $2,368          | +25.7% |
| 317   | 53.1%   | $5,167       | $4,470          | +15.6% |
| 448   | 44.8%   | $4,303       | $2,731          | +57.5% |
| **Pooled** | —  | **$12,446**  | **$9,569**     | **+30.1%** |

**Model:** LightGBM + Optuna. 95% bootstrap CI: **[+11.9%, +51.0%]**, positive in 99.9% of resampled draws.

**Key Insight:**  
Applying Campaign 18 during afternoon hours produced a pooled **+30.1%** sales uplift across three validated pilot stores over the 56-day campaign window.

---

### 8. Business Impact

- Scaling Campaign 18 to **85 eligible underperforming stores** is projected to generate **≈$41K in incremental revenue** within 60 days  
- Drives a **30.1% pooled sales uplift** at the store level through afternoon deployment to Best Customers

---

### 9. Limitations

- **Campaign mechanics not explicitly provided**: Offer structure (discount depth, product eligibility) was inferred using Dunnhumby's official campaign design best practices.
- **External factors excluded**: Forecast does not incorporate weather, local competition, or macro trends; future iterations could enhance robustness with causal data.
- **Forecast uncertainty**: wMAPE of 45–53% and a wide uplift confidence interval reflect real day-to-day sales noise at this sample size — results should inform a pilot decision, not a final rollout commitment.

---

**Stack:** Python 3.9 · Pandas · LightGBM · Optuna

# Dunnhumby Retail Store Performance Analysis – Notebooks

This directory contains the Jupyter notebooks used throughout the project, covering the complete analytics workflow from data preparation and exploratory analysis to customer segmentation, campaign evaluation, sales forecasting, and business impact assessment.

---

## Notebook Overview

| Notebook | Description |
|----------|-------------|
| `notebooks/data_cleaning.ipynb` | Data preparation, quality checks, feature engineering, and creation of the modeling dataset. |
| `notebooks/store_performance_analysis.ipynb` | Exploratory analysis, campaign evaluation, customer segmentation, forecasting, and business recommendations. |

---

# Data Cleaning Notebook

**File:** `notebooks/data_cleaning.ipynb`

## Objective

Transform raw multi-source retail transaction data into a validated, analysis-ready dataset suitable for exploratory analysis, machine learning, and forecasting.

---

## 1. Data Understanding

| Data Source | Rows | Key Fields |
|-------------|------:|-----------|
| Transaction | 2,595,914 | household_key, basket_id, product_id, quantity, sales_value, coupon_disc, day |
| Product | 23,539 | department, brand, commodity, sub_commodity |
| Household | 103,200 | age_bracket, income_bracket, household_size |
| Campaign Description | 30 | campaign_id, description, start_day, end_day |
| Coupons | 1,310,318 | campaign_id, household_key, product_id |

---

## 2. Data Preparation

| Quality Check | Rows Removed | % of Raw Data |
|---------------|-------------:|--------------:|
| Zero quantity | 7,266 | 0.28% |
| Coupon discount greater than sales value | 6,206 | 0.24% |
| Extreme outliers | 10 | 0.00% |
| **Total Removed** | **13,472** | **0.52%** |

---

## 3. Feature Engineering

| Feature | Description | Business Purpose |
|---------|-------------|------------------|
| `DATE` | Julian day converted to calendar date | Time-series analysis |
| `DAY_CATEGORY` | Weekday / Weekend | Traffic pattern analysis |
| `TIME_CATEGORY` | Day (06:00–17:59) / Night (18:00–05:59) | Store operating analysis |
| `TIME_OF_DAY_CATEGORY` | Morning / Afternoon / Evening / Night | Promotion scheduling |
| `cust_purchase_value` | Net customer spend | Customer value estimation |
| `sales_lag_7` | Sales seven days earlier | Forecasting feature |
| `sales_ma_7` | Seven-day moving average | Trend smoothing |

---

# Store Performance Analysis Notebook

**File:** `notebooks/store_performance_analysis.ipynb`

## Objective

Identify store performance drivers, segment customers based on purchasing behavior, evaluate promotional campaigns, forecast sales, and recommend actions for improving underperforming stores.

---

## 4. Exploratory Data Analysis

### 4.1 Store Performance Distribution

| Category | Stores | % of Stores | Sales Contribution |
|----------|-------:|------------:|-------------------:|
| Performing Stores | 71 | 12% | 80% |
| Underperforming Stores | 511 | 88% | 20% |
| **Total** | **582** | **100%** | **100%** |

**Key Insight**

The top 12% of stores generate approximately 80% of total sales, confirming a strong Pareto distribution and highlighting significant optimization opportunities among underperforming stores.

---

### 4.2 Customer Traffic Patterns

| Dimension | Category | Share |
|-----------|----------|------:|
| Week Part | Weekday | 65% |
| | Weekend | 35% |
| Time of Day | Afternoon (12:00–18:00) | **27%** |
| | Evening (19:00–24:00) | 25% |
| | Morning (06:00–11:00) | 24% |
| | Night (00:00–05:00) | 24% |

**Key Insight**

Afternoon is the highest customer engagement period, making it the preferred window for campaign deployment.

---

## 5. Campaign Performance

| Campaign | Customer Conversion | Coupon Conversion | Gross ROI | Sales Share | Incremental Revenue |
|----------|--------------------:|------------------:|----------:|------------:|--------------------:|
| 15 | 0.8% | 4.8% | 134% | 13% | $1.1M |
| 16 | 4.4% | 8.7% | 272% | 17% | $2.0M |
| 17 | 1.8% | 5.0% | 199% | 22% | $2.6M |
| **18** | **13.0%** | **9.1%** | **411.4%** | **47%** | **$5.5M** |

> **Net ROI (Campaign 18): 278.7%** after deducting 75% cost of goods sold and a $1,500 campaign cost.

**Key Insight**

Campaign 18 consistently outperformed all other campaigns across conversion, revenue contribution, and return on investment, making it the strongest candidate for expansion.

---

## 6. Customer Segmentation (RFM)

| Segment | Customers | Revenue | Average Spend | Campaign 18 Redemption |
|---------|----------:|---------:|--------------:|-----------------------:|
| **Best** | **20.2%** | **41%** | **$1,246** | **38%** |
| Loyal | 20.3% | 29% | $682 | 32% |
| Promising | 21.0% | 19% | $413 | 18% |
| At-Risk | 19.6% | 10% | $199 | 12% |
| Lost | 18.8% | 2% | $75 | 0% |

**Key Insight**

Best Customers represent only 20.2% of households but contribute 41% of total revenue and achieve the highest campaign redemption rate.

---

## 7. Sales Forecasting

### Pilot Store Selection

Stores **299**, **317**, and **448** were selected because they:

- Ranked among the lowest-performing stores by sales
- Contained the highest number of Best Customers within the eligible cohort
- Had complete historical sales records
- Participated fully in Campaign 18

### Forecast Results

| Store | wMAPE | Actual Sales | Counterfactual Sales | Sales Uplift |
|------:|------:|-------------:|---------------------:|-------------:|
| 299 | 52.9% | $2,977 | $2,368 | +25.7% |
| 317 | 53.1% | $5,167 | $4,470 | +15.6% |
| 448 | 44.8% | $4,303 | $2,731 | +57.5% |
| **Combined** | — | **$12,446** | **$9,569** | **+30.1%** |

- 95% Bootstrap Confidence Interval: **+11.9% to +51.0%**
- Positive uplift observed in **99.9%** of bootstrap samples

**Key Insight**

Deploying Campaign 18 during afternoon hours produced a combined **30.1% increase in sales** across the three pilot stores during the 56-day evaluation period.

---

## 8. Business Impact

- Estimated **$41K incremental revenue** by expanding Campaign 18 to **85 eligible underperforming stores** over 60 days.
- Projected **30.1% pooled sales uplift** through targeted deployment to Best Customers during afternoon shopping hours.

---

## 9. Limitations

- Campaign mechanics (offer structure, discount depth, and eligible products) were inferred from Dunnhumby campaign documentation.
- Forecasts do not account for external variables such as weather, competitor actions, or macroeconomic conditions.
- Forecast uncertainty (wMAPE 45–53%) and the uplift confidence interval indicate results should support pilot decisions rather than full-scale rollout planning.

---

**Stack:** Python 3.9 · Pandas · LightGBM · Optuna
