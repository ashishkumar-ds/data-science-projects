# Dunnhumby Retail Store Performance Analysis

[![CI](https://github.com/ashishkumar-ds/data-science-projects/actions/workflows/ci.yml/badge.svg)](https://github.com/ashishkumar-ds/data-science-projects/actions/workflows/ci.yml)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LightGBM](https://img.shields.io/badge/model-lightgbm-76B900)](https://lightgbm.readthedocs.io)
[![Live API](https://img.shields.io/badge/api-render-46e3b7?logo=render&logoColor=white)](https://retail-forecast-api-7sue.onrender.com/health)
[![Tableau](https://img.shields.io/badge/dashboard-tableau-E97627?logo=tableau&logoColor=white)](https://public.tableau.com/views/DunnhumbyStorePerformanceReportwithfilter/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

> Part 1 of the Dunnhumby series. See [Part 2 — Retail Campaign Automation with n8n](https://github.com/ashishkumar-ds/retail-campaign-automation-with-n8n) for the full campaign automation workflow.
>

## Project Summary

This project analyzes **2.59M+ household-level transactions** from the Dunnhumby Retail Store dataset to drive a targeted intervention in underperforming stores. By combining **RFM customer segmentation**, **campaign ROI analysis**, and **time-of-day optimization**, the work delivers a prioritized, 60-day action plan built around a 56-day campaign window.

A **Difference-in-Differences (DiD) validation** with untreated control households and matched control stores then tests the campaign's *causal* impact, estimating **≈$14K in incremental revenue per 56-day cycle** (vs. $41K under forecast-based attribution).

An interactive **Tableau dashboard** enables monitoring of store performance, customer segments, and campaign response, empowering managers to act on insights immediately.

---

## Problem Statement

- **87.8% of stores (511 of 582)** are underperforming, generating only **20% of total sales**  
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
| **Forecast Impact**      | +30.1% projected uplift across three pilot stores, with +9.7% market drift |
| **DiD Validation**       | True causal lift **+2.84% per targeted household** (p=0.10) ≈ **$14.1K/cycle**; pilot stores show no detectable store-level lift (-9.6%, n.s.) |
---

## Recommendations

1. **Keep targeting Best Customers** — highest redemption (38%, 18.9% overall for Campaign 18) and revenue contribution; the ~+3% household lift is benchmark-consistent with dunnhumby's published campaign results
2. **Prioritize the 85 eligible stores** — pilot first, then expand by Best Customer density
3. **Deploy in afternoon (12–18)** where engagement peaks
4. **Monitor results via the Tableau dashboard** — track sales, redemption, and store-level trends as the rollout expands

> *Causal estimate: **≈$14K incremental revenue per 56-day cycle** across all targeted households (DiD ITT), before campaign costs.*

---

## Benchmark vs. Dunnhumby Case Studies

How Campaign 18's measured results compare against dunnhumby's published campaign outcomes (sources in [References](#references)):

| Metric | This project (Campaign 18) | dunnhumby benchmark | Assessment |
|--------|---------------------------|---------------------|------------|
| **Total sales lift** (causal, DiD ITT) | **+2.84%** per targeted household / 56-day cycle (p=0.10) | +3.6% [1] to +11% [2] published campaign uplift | **Matches** the realistic band for well-targeted campaigns |
| **Coupon redemption rate** | **18.9%** of targeted households (214 / 1,133) | 16% retail-media norm [3] · 36% mature loyalty program [4] | **Exceeds** the retail-media norm, below best-in-class loyalty |
| **Return on spend** | **≈9.4:1** revenue ROAS | £6:1 ROAS on featured products [1] | **Same order of magnitude** |
| **Customer concentration** (Pareto) | Top 20.2% of customers = 41% of revenue | 17% of shoppers = 64% of sales [4] | **Same pattern**, flatter tail |
| **Targeting precision** | Treated households spend 3.6× controls pre-campaign | Audiences built from previous category buyers [2] | **Consistent** with dunnhumby's targeting method |
| **Featured-product uplift** | Not measurable (no product-level treatment data) | +45% on featured SKUs [1] | **Out of scope** |

> **Methodology note**: a peer-reviewed DiD study [5] on this same 2,500-household Dunnhumby panel found targeted coupons significantly increased purchases — externally validating both our approach and the finding that dunnhumby-style targeting produces real but modest total-basket lift.

**Takeaway**: Campaign 18 performs **in line with dunnhumby's published results** — strong targeting and redemption, single-digit total-basket lift.

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
│   ├── data cleaning.ipynb
│   ├── store performance analysis.ipynb
│   └── store_performance_analysis_with_DiD.ipynb   # DiD validation (charts embedded)
│
├── dashboard/                          # Tableau dashboard for store monitoring
│   └── dashboard_screenshot.png
│
├── presentation/                       # Executive-ready deck for stakeholders
│   └── presentation deck.pdf
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
├── scripts/                            # Re-runnable estimators (no notebook needed)
│   └── did_estimate.py                 # Household ITT DiD, stdlib only
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
```

## References

1. dunnhumby — [Nicorette Coupon at Till](https://www.dunnhumby.com/tesco-case-studies/nicorette/) (featured-product POS uplift, £6:1 ROAS benchmark)
2. dunnhumby — [Reaching the right customers across every channel](https://www.dunnhumby.com/case-studies/reaching-right-customers-across-every-channel/) (omnichannel campaign, audience targeting method)
3. dunnhumby — [How retail media accelerated premium ice-cream brands' growth](https://www.dunnhumby.com/case-studies/how-retail-media-accelerated-premium-ice-cream-brands-growth/) (16% coupon-at-till benchmark)
4. dunnhumby — [Turning a tired loyalty programme into a growth engine](https://www.dunnhumby.com/case-studies/turning-tired-loyalty-programme-into-growth-engine/) (NA grocer: 36% loyalty redemption, customer concentration)
5. IJBNPA (2018) — [Difference-in-Differences on the same 2,500-household Dunnhumby panel](https://link.springer.com/article/10.1186/s12966-018-0744-7) (external methodology validation)

## License

MIT — see [LICENSE](LICENSE).
