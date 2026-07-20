
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

| Store | wMAPE   | MAE   | Actual Sales | Counterfactual | Uplift |
|-------|---------|-------|--------------|-----------------|--------|
| 299   | 57.8%   | 38.4  | $2,977       | $2,918          | +2.0%  |
| 317   | 53.2%   | 41.1  | $5,167       | $4,577          | +12.9% |
| 448   | 40.7%   | 34.8  | $4,303       | $2,663          | +61.6% |
| **Pooled** | **41–58%** | —  | **$12,446**  | **$10,157**     | **+22.5%** |

**Model:** LightGBM + Optuna. Pooled uplift is computed as the % difference between summed actual and summed counterfactual sales across all three stores — not an average of the three individual percentages — so the result is dollar-weighted rather than treating differently sized stores as equal.

**Key Insight:**  
Applying Campaign 18 during afternoon hours produced a pooled **+22.5%** sales uplift across three validated pilot stores over the 56-day campaign window. Individual store results (+2.0% to +61.6%) reflect genuine forecast uncertainty at this sample size, not measurement error.

---

### 8. Business Impact

- Scaling Campaign 18 to **85 eligible underperforming stores** is projected to generate **≈$31K in incremental revenue** within 60 days  
- Drives a **22.5% pooled sales uplift** at the store level through afternoon deployment to Best Customers  

---

### 9. Limitations

- **Campaign mechanics not explicitly provided**: Offer structure (discount depth, product eligibility) was inferred using Dunnhumby's official campaign design best practices.
- **External factors excluded**: Forecast does not incorporate weather, local competition, or macro trends; future iterations could enhance robustness with causal data.
- **Forecast uncertainty**: wMAPE ranges 41–58% across pilot stores at daily grain, consistent with single-store forecasting at this sample size, but wide enough that results should inform a pilot decision, not a final rollout commitment.

---

**Stack:** Python 3.9 · Pandas · LightGBM · Optuna
