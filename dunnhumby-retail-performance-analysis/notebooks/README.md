# Dunnhumby Retail Store Performance – Notebooks

# 🧮 Retail Analytics Project  
End-to-end workflow covering data cleaning, feature engineering, exploratory analysis, campaign uplift, segmentation, forecasting, and business impact.

---

# Tier 1 – Data Cleaning Notebook  
**File:** `notebooks/data_cleaning.ipynb`

## 🎯 Objective  
Transform raw multi-source retail transaction data into a unified, validated, and analysis-ready dataset suitable for modeling and downstream analytics.

---

# 2. Data Understanding

| Data Source | Rows | Key Fields |
|--------------|-------|-------------|
| Transaction | 2,595,914 | household_key, basket, product, qty, sales, discount, coupon, day |
| Product | 23,539 | dept, brand, commodity, size |
| Coupon | 4 campaigns | coupon_upc, campaign, start/end day |
| Campaign description | 4 rows | description, objective |

---

## 3. Data Preparation

| QC Gate | Rows Removed | % of Raw |
|---------|--------------|-----------|
| Zero quantity | 7,266 | 0.28% |
| Illegal positive discount | 6,206 | 0.24% |
| Extreme outliers | 10 | 0.00% |
| **TOTAL REMOVED** | **13,472** | **0.52%** |

---

## 4. Feature Engineering

| Feature | Definition | Business Role |
|---------|------------|----------------|
| `DATE` | Julian → calendar date | time-series index |
| `DAY_CATEGORY` | weekday / weekend | roster optimisation |
| `TIME_CATEGORY` | Day (06–18) / Night (18–06) | store-hour decisions |
| `TIMES_CATEGORY` | morning / afternoon / evening / night | promo timing |
| `cust_purchase_value` | net spend (sales + coupon) | LTV modelling |
| `sales_lag_7` | sales 7 days ago | auto-regressive signal |
| `sales_ma_7` | 7-day moving average | trend smoothing |

**Artifact produced:** `clean_2_58M_rows_562stores.parquet`  

[→ Jump to Tier 2 Analysis](tier-2-analysis.md)

---

# Tier 2 – Main Analysis Notebook  
**File:** `notebooks/main_analysis.ipynb`

## 🎯 Objective  
Identify performance drivers, segment customers by value, and quantify campaign uplift to generate recommendations for improving underperforming stores.

---

# 5. Exploratory Data Analysis

## 5.1 Store Concentration (Pareto)

| Lens | Metric | Business Take-away |
|------|--------|--------------------|
| Store universe | 562 total stores | 178 active after QC filters |
| Store performance | top 19% stores = 80% sales | 80/20 confirmed → capex focus list |

---

## 4.2 Customer Traffic Patterns

| Dimension | Level | Footfall Share |
|-----------|--------|------------------|
| Week-part | weekday | 65% |
|  | weekend | 35% |
| Time-of-day | **afternoon (10–15)** | **31.8%** |
|  | evening (16–21) | 28.6% |
|  | morning (04–09) | 22.3% |
|  | night (22–03) | 17.3% |

**Insight:** Afternoon weekday drives highest traffic → roster & promo budget skew **32% to 10 AM–3 PM**.

---

# 6. Campaign Uplift (Controlled Pre/Post)

| Campaign | Cust. CR | Coupon CR | ROI | Sales Share | Incremental | Uplift vs Baseline |
|----------|-----------|------------|------|-------------|--------------|---------------------|
| 15 | 0.8% | 4.8% | 25% | 13% | 1.1M | +2.1% |
| 16 | 4.4% | 8.7% | 194% | 17% | 2.0M | +5.8% |
| 17 | 1.8% | 5.0% | 114% | 22% | 2.6M | +4.2% |
| **18** | **13.0%** | **9.1%** | **235%** | **47%** | **5.5M** | **+18.7%** |

### Statistical Validation
- Baseline: day 531–586 (**n = 38,661**)  
- Campaign: day 587–642 (**n = 38,660**)  
- Best-customer daily growth: **+1.22% → +2.60%** (Δ +113%, *p* < 0.05, two-sided t-test)  
- 95% CI for uplift: **[+16.4%, +21.0%] → 5.0M – 6.1M incremental sales**

---

# 7. Customer Segmentation (RFM)

| Segment | % Customers | % Revenue | Avg Monetary | Campaign-18 Redemption |
|----------|-------------|------------|---------------|-------------------------|
| Best | 11% | 41% | 1,246 | 38% |
| Loyal | 25% | 29% | 682 | 32% |
| Promising | 31% | 19% | 413 | 18% |
| At-Risk | 25% | 10% | 199 | 12% |
| Lost | 8% | 2% | 75 | 0% |

**Insight:** Top 11% of customers drive 41% of revenue and 38% of high-ROI redemptions → prioritise retention & upspend on this tier.

---

# 8.Predictive Modelling — Sales Forecast

| Model | wMAPE | RMSE | MAE | R² |
|--------|--------|-------|------|-----|
| Linear Regression | 5.4% | 842 | 512 | 0.78 |
| **LightGBM + Optuna** | **3.1%** | **488** | **296** | **0.92** |

**Notes:**  
- Optuna tuned **50 hyper-parameter sets**  
- Time-series split: **70/15/15%**  
- Production forecast: **60-day horizon**, nightly refresh for inventory & labour planning  
- Includes **95% prediction interval**

---

# 9. Business Impact

- Scale Campaign-18 mechanics → **+12M annualised** (CI 10M–14M)  
- Deploy 3.1% MAPE forecast → **342k working-capital release** via safety-stock reduction  
- Re-fit / exit bottom-quintile stores (<1% sales) → OpEx savings TBD  

---

**Stack:** Python 3.9 · pandas · LightGBM · Optuna  
**Repository:** Ready for staging pipeline deployment

