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
