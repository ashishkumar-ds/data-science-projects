# Dunnhumby Retail Store Performance Analysis

> Part 1 of the Dunnhumby series. See [Part — 2 Retail Campaign Automation with n8n](https://github.com/ashishkumar-ds/retail-campaign-automation-with-n8n) for the full campaign automation workflow.
> 

## Project Summary

This project analyzes **2.59M+ household-level transactions** from the Dunnhumby Retail Store dataset to drive a targeted intervention in underperforming stores. By combining **RFM customer segmentation**, **campaign ROI analysis**, and **time-of-day optimization**, the work delivers a prioritized, 60-day action plan.

A **Difference-in-Differences (DiD) validation** with untreated control households and matched control stores then tests the campaign's *causal* impact, estimating **≈$14K in incremental revenue per 56-day cycle** (vs. $41K under forecast-based attribution) and recommending a randomized rollout before scaling.

An interactive **Tableau dashboard** enables real-time monitoring of store performance, customer segments, and campaign response, empowering managers to act on insights immediately.

---

## Problem Statement

- **88% of stores (511 of 582)** are underperforming, generating only **20% of total sales**  
- These stores show **monthly sales growth below 9.3%**

**Business Question**:  
> How can we increase sales in underperforming stores within **60 days**?

---

## Dataset Description

- **Source**: [Dunnhumby Retail Store Public Dataset](https://www.dunnhumby.com/source-files/)  
- **Total Transactions**: 2,595,914
- **Stores**: 582 unique store locations
- **Households**: 2,500 (loyalty panel; 1,584 ever assigned to a campaign)
- **Products**: 23,539
- **Time Frame**: 2017–2018  

---

## Key Findings

| Focus Area               | Insight                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Store Performance**    | Top 12% of stores (71) drive 80% of revenue; 511 are underperforming    |
| **Best Customers**       | Age 45–54, income $50K–$74K, no kids, 20.2% of base, 41% of revenue    |
| **Top Campaign**         | **Campaign 18**: 411.4% gross ROI, 278.7% net ROI *(redeemer-attributed, not causal)*    |
| **Optimal Timing**       | **Afternoon (12–18)** drives peak engagement and highest uplift         |
| **Forecast Impact**      | +30.1% projected uplift across three pilot stores — **not confirmed causally**: market drift was +9.7% |
| **DiD Validation**       | True causal lift **+2.84% per targeted household** (p=0.10) ≈ **$14.1K/cycle**; pilot stores show no detectable store-level lift (-9.6%, n.s.) |
---

## Recommendations

1. **Keep targeting Best Customers** — highest redemption (38%, 18.9% overall for Campaign 18) and revenue contribution; the ~+3% household lift is benchmark-consistent with dunnhumby's published campaign results
2. **Do not scale to 85 stores on forecast evidence** — DiD shows the lift does not concentrate in targeted stores (only 12 of 653 Campaign-18 redemptions occurred in the three pilots)
3. **Deploy in afternoon (12–18)** where engagement peaks
4. **Run a randomized rollout** across stores/households, powered for ~+3% effects, monitored via the Tableau dashboard

> *Causal estimate: **≈$14K incremental revenue per 56-day cycle** across all targeted households (DiD ITT), before campaign costs — scale only with experimental measurement in place.*

---

## Benchmark vs. Dunnhumby Case Studies

How Campaign 18's measured results compare against dunnhumby's published campaign outcomes:

| Metric | This project (Campaign 18) | Dunnhumby benchmark | Assessment |
|--------|---------------------------|---------------------|------------|
| **Total sales lift (causal, DiD ITT)** | **+2.84%** per targeted household per 56-day cycle (p=0.10; +7.0% matched-control upper bound) | +3.6% ([Nicorette POS uplift](https://www.dunnhumby.com/tesco-case-studies/nicorette/)) to +11% ([omnichannel featured-brand campaign](https://www.dunnhumby.com/case-studies/reaching-right-customers-across-every-channel/)) | ✅ **Matches** the realistic band for well-targeted campaigns |
| **Coupon redemption rate** | **18.9%** (214 of 1,133 targeted households) | 16% coupon-at-till ([Tesco ice cream launch](https://www.dunnhumby.com/case-studies/how-retail-media-accelerated-premium-ice-cream-brands-growth/)); 36% mature loyalty program ([NA grocer](https://www.dunnhumby.com/case-studies/turning-tired-loyalty-programme-into-growth-engine/)) | ✅ **Exceeds** retail-media norm, below best-in-class loyalty |
| **Return on spend** | **≈9.4:1** revenue ROAS (~2.3:1 after 75% COGS) | £6:1 ROAS ([Nicorette × Tesco](https://www.dunnhumby.com/tesco-case-studies/nicorette/), featured products) | ✅ **Same order of magnitude** |
| **Customer concentration (Pareto)** | Top 20.2% of customers = 41% of revenue | 17% of shoppers = 64% of sales ([NA grocer loyalty](https://www.dunnhumby.com/case-studies/turning-tired-loyalty-programme-into-growth-engine/)) | ✅ **Same pattern**, flatter tail |
| **Targeting precision** | Treated households spend 3.6× controls pre-campaign | Audience built from "previous buyers in relevant categories" ([confectionery campaign](https://www.dunnhumby.com/case-studies/reaching-right-customers-across-every-channel/)) | ✅ **Consistent** with dunnhumby's targeting method |
| **Featured-product uplift** | Not measurable (no product-level treatment data) | +45% on featured SKUs ([Nicorette Coupon at Till](https://www.dunnhumby.com/tesco-case-studies/nicorette/)) | ➖ Out of scope |

> **Methodology note**: a [peer-reviewed study (IJBNPA, 2018)](https://link.springer.com/article/10.1186/s12966-018-0744-7) ran a DiD on this same 2,500-household Dunnhumby panel and found targeted coupons significantly increased purchases — externally validating both our approach and the finding that dunnhumby-style targeting produces real but modest total-basket lift.

**Takeaway**: Campaign 18 performs **in line with dunnhumby's published results** — strong targeting and redemption, single-digit total-basket lift. The earlier +30.1% store-level claim was the outlier, not the DiD estimate.

---

## Tools and Technologies

- **Python**: Pandas, Scikit-Learn, LightGBM, Optuna, Statsmodels 
- **Visualization**: Matplotlib, Seaborn, Tableau  
- **Methods**: RFM Segmentation, ROI Analysis, Time-Series Forecasting, **Difference-in-Differences (TWFE, event study, matched controls)**  

---

## Project Structure

```bash
dunnhumby-retail-performance/
│
├── notebooks/                          # Data cleaning + store performance analysis
│   ├── data_cleaning.ipynb
│   ├── store_performance_analysis.ipynb   # incl. DiD validation section
│   ├── did_household_event_study.png
│   └── did_store_pilots.png
│
├── dashboard/                          # Tableau dashboard for real-time store monitoring
│   └── dashboard_screenshot.png
│
├── presentation/                       # Executive-ready deck for stakeholders
│   └── presentation_deck.pdf
│
├── datasets/                           # Raw Dunnhumby source data
│   ├── transaction_data.csv
│   ├── product.csv
│   ├── coupon.csv
│   ├── coupon_redempt.csv
│   ├── campaign_desc.csv
│   ├── campaign_table.csv
│   └── hh_demographic.csv
│
├── api/                                # FastAPI service serving the forecast model
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── sales_forecast_model.pkl
│   │   └── daily_store_features.pkl
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
└── README.md
