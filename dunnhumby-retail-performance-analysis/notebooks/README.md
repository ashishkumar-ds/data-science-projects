End-to-end workflow covering data cleaning, feature engineering, exploratory analysis, campaign uplift, segmentation, forecasting, and business impact.

---

## Data Cleaning Notebook  
**File:** `notebooks/data_cleaning.ipynb`

### 🎯 Objective  
Transform raw multi-source retail transaction data into a unified, validated, and analysis-ready dataset suitable for modeling and downstream analytics.

---

### 2. Data Understanding

| Data Source       | Rows       | Key Fields                                                |
|-------------------|------------|-----------------------------------------------------------|
| Transaction       | 2,595,914  | household_key, basket_id, product_id, quantity, sales_value, coupon_disc, day |
| Product           | 23,539     | department, brand, commodity, sub_commodity               |
| Household         | 103,200    | age_bracket, income_bracket, household_size               |
| Campaign_desc     | 30         | campaign_id, description, start_day, end_day              |
| Coupons           | 1,310,318  | campaign_id, household_key, product_id                    |

---

### 3. Data Preparation

| QC Gate                     | Rows Removed | % of Raw |
|-----------------------------|--------------|----------|
| Zero quantity               | 7,266        | 0.28%    |
| Illegal positive discount   | 6,206        | 0.24%    |
| Extreme outliers            | 10           | 0.00%    |
| **TOTAL REMOVED**           | **13,472**   | **0.52%**|

---

### 4. Feature Engineering

| Feature             | Definition                                | Business Role                  |
|---------------------|-------------------------------------------|--------------------------------|
| `DATE`              | Julian → calendar date                    | time-series index              |
| `DAY_CATEGORY`      | weekday / weekend                         | roster optimisation            |
| `TIME_CATEGORY`     | Day (06–18) / Night (18–06)               | store-hour decisions           |
| `TIMES_CATEGORY`    | morning / afternoon / evening / night     | promo timing                   |
| `cust_purchase_value`| net spend (sales_value + coupon_disc)    | LTV modelling                  |
| `sales_lag_7`       | sales 7 days ago                          | auto-regressive signal         |
| `sales_ma_7`        | 7-day moving average                      | trend smoothing                |

**Artifact produced:** `clean_2_58M_rows_562stores.parquet`  


---

## Main Analysis Notebook  
**File:** `notebooks/main_analysis.ipynb`

### 🎯 Objective  
Identify performance drivers, segment customers by value, and quantify campaign uplift to generate recommendations for improving underperforming stores.

---

### 5. Exploratory Data Analysis

#### 5.1 Store Concentration (Pareto)

| Category              | Store Count | % of Total | Sales Contribution |
|-----------------------|-------------|------------|---------------------|
| Performing (Top 12%)  | 69          | 12%        | 80%                 |
| Underperforming       | 511         | 88%        | 20%                 |
| **Total**             | **582**     | **100%**   | **100%**            |

**Key Insight:**  
A small fraction of stores drives the majority of revenue,confirming a strong Pareto dynamic and justifying focused intervention on the underperforming long tail.

---

#### 5.2 Customer Traffic Patterns

| Dimension    | Level     | Footfall Share |
|--------------|-----------|----------------|
| Week-part    | weekday   | 65%            |
|              | weekend   | 35%            |
| Time-of-day  | **afternoon (12–18)** | **27%**    |
|              | evening (19–24)       | 25%            |
|              | morning (06–11)       | 24%            |
|              | night (00–05)         | 24%            |

**Key Insight:**  
Afternoon (12–18) is the peak engagement window for campaign delivery.

---

### 6. Campaign Uplift

| Campaign | Cust. CR | Coupon CR | Gross ROI | Sales Share | Incremental |
|----------|----------|-----------|-----------|-------------|-------------|
| 15       | 0.8%     | 4.8%      | 134%      | 13%         | $1.1M       |
| 16       | 4.4%     | 8.7%      | 272%      | 17%         | $2.0M       |
| 17       | 1.8%     | 5.0%      | 199%      | 22%         | $2.6M       |
| **18**   | **13.0%**| **9.1%**  | **411.4%**| **47%**     | **$5.5M**   |

> Net ROI for Campaign 18 = **278.7%** (after deducting 75% COGS and $1,500 campaign cost).

**Key Insight:**  
Campaign 18 drives the highest revenue share and ROI,making it the strongest candidate for scaling to underperforming stores.

---

### 7. Customer Segmentation (RFM)

| Segment   | % Customers | % Revenue | Avg Monetary | Campaign-18 Redemption |
|-----------|-------------|-----------|--------------|------------------------|
| **Best**      | **20.2%**       | **41%**       | **$1,246**       | **38%**                    |
| Loyal     | 20.3%       | 29%       | $682         | 32%                    |
| Promising | 21.0%       | 19%       | $413         | 18%                    |
| At-Risk   | 19.6%       | 10%       | $199         | 12%                    |
| Lost      | 18.8%       | 2%        | $75          | 0%                     |

**Key Insight:**  
Best Customers (20.2% of base) drive 41% of revenue and 38% of redemptions,the highest-value segment for retention and targeting.

---

### 8. Predictive Modelling — Sales Forecast

**Why Store #289?**  
Selected as the ideal pilot among underperforming stores: Bottom 19% by sales, 118 Best Customers (highest in cohort), and full Campaign 18 exposure with 71 days of clean daily sales.

| Model               | wMAPE   | MAE   | RMSE  | R²    |
|---------------------|---------|-------|-------|-------|
| **LightGBM + Optuna** | **15.1%** | **296** | **488** | **0.92** |

**Key Insight:**  
Applying Campaign 18 during afternoon hours is projected to lift sales by **+11%** for Store #289 over 60 days.

---

### 9. Business Impact

- Scaling Campaign 18 to **85 eligible underperforming stores** is projected to generate **≈$15K in incremental revenue** within 60 days  
- Drives an **11% sales uplift** at the store level through afternoon deployment to Best Customers  

---

### Limitations

- **Campaign mechanics not explicitly provided**: Offer structure (discount depth, product eligibility) was inferred using Dunnhumby’s official campaign design best practices.
- **External factors excluded**: Forecast does not incorporate weather, local competition, or macro trends; future iterations could enhance robustness with causal data.

---

**Stack:** Python 3.9 · pandas · LightGBM · Optuna  