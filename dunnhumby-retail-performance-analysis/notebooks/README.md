# Dunnhumby Retail Store Performance Analysis – Notebooks

This directory contains the Jupyter notebooks used throughout the project, covering the complete analytics workflow from data preparation and exploratory analysis to customer segmentation, campaign evaluation, causal (DiD) validation, forecasting, and business impact assessment.

---

## Notebook Overview

| Notebook | Status | Description |
|----------|--------|-------------|
| `store_performance_analysis_with_DiD.ipynb` | **Canonical — start here** | Full analysis: data prep, RFM segmentation, campaign evaluation, LightGBM counterfactual forecasting, and the DiD causal validation (+2.84% household ITT / −9.6% store-level) that gates rollout in Parts 2–3. |
| `data cleaning.ipynb` | Superseded | Early data-preparation pass. Kept for history; the canonical notebook re-runs the same cleaning with named constants. |
| `store performance analysis.ipynb` | Superseded | Pre-DiD version of the analysis (forecast-based uplift only). Kept for history; its uplift numbers are revised by the DiD section of the canonical notebook. |

**Key numbers to quote (from the canonical notebook):** forecast uplift +30.1% [+11.9%, +51.0%] is directional and absorbs +9.7% market drift; the causal answer is +2.84% household ITT (p=0.10) / −9.6% store-level DiD → ≈$14K causal incremental revenue per 56-day cycle. Scale-up gating in Parts 2–3 uses the causal 3% target.

---

# Data Cleaning Notebook

**File:** `notebooks/data cleaning.ipynb` (superseded — logic preserved in the canonical notebook)

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
Why Stores #299, #317, and #448?
These three stores were chosen as pilot candidates based on four criteria: ranking at the bottom edge of the top-15% by sales (i.e., the largest stores in the underperforming tail), high Best-Customer counts, over 480 days of history, and assumed full Campaign-18 exposure. **Verification against the data confirms size/history but not the other two:** Best-Customer counts are 6/8/8 (stores #309 and #289 have more), and actual Campaign-18 redemptions captured in-store are **0 / 5 / 7** of 653 — see §7.1.

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

## 7.1 Difference-in-Differences (DiD) Validation

The forecast counterfactual above compares each store only to its own history, so it cannot separate the campaign effect from market-wide movements (all-store sales drifted **+9.7%** during the campaign window). The DiD section appended to the notebook adds a quasi-experimental validation with untreated controls.

| DiD requirement | Evidence |
|-----------------|----------|
| Panel data | 2,500 households × 102 weeks; 582 stores × 711 days |
| Sharp treatment timing | Campaign 18: days 587–642 (56 days) |
| Untreated controls | Only 1,133/2,500 households assigned Campaign 18; only 90 stores saw any redemption |

### Results

| Estimate | Design | Result |
|----------|--------|--------|
| **Household ITT DiD** (primary) | 1,123 treated vs 981 clean control households, symmetric 56-day windows | **+$12.46/HH (+2.84%)**, p=0.100 → **≈$14.1K incremental revenue per 56-day cycle** |
| Household ITT — matched controls | 1-NN on pre-spend/trips/trend | +$30.89/HH (+7.03%), p=0.004 (upper bound; RTM risk) |
| Weekly TWFE panel | 1,669 HH, HH+week FE, bootstrap CI | -$0.90/HH-week [-3.00, +1.34] — ≈0 |
| Parallel-trends placebo test | Event study, ref week 83 | p=0.897 — flat pre-trend, control group credible |
| **Store-level DiD (pilots)** | 3 pilots vs 12 matched underperforming stores (no C18 redemptions) | **-9.6%** (p=0.178), 95% CI [-23.6%, +25.4%] |

**Key Insight**

Campaign 18's *causal* uplift is small at best (~+3% at the household level, ≈$14K per cycle) — not the +30.1%/411% ROI implied by forecast-based attribution, which largely reflects market drift and model bias. Pilot-store targeting does not concentrate the lift: only 12 of 653 Campaign-18 redemptions occurred inside the pilot stores (store 299 received zero). Scale-up projections should be revised accordingly and a randomized rollout used to measure true lift.

---

## 8. Business Impact

- Estimated **$41K incremental revenue** by expanding Campaign 18 to **85 eligible underperforming stores** over 60 days.
- Projected **30.1% pooled sales uplift** through targeted deployment to Best Customers during afternoon shopping hours.

---

## 9. Limitations

- Campaign mechanics (offer structure, discount depth, and eligible products) were inferred from Dunnhumby campaign documentation.
- Forecasts do not account for external variables such as weather, competitor actions, or macroeconomic conditions.
- Forecast uncertainty (wMAPE 45–53%) and the uplift confidence interval indicate results should support pilot decisions rather than full-scale rollout planning.
- The DiD validation (§7.1) finds the causal campaign effect is far smaller than forecast-based attribution suggests; treated households are 45% of the customer base, so spillover to "control" units may bias the ITT estimate downward.

---

**Stack:** Python 3.9 · Pandas · LightGBM · Optuna
