# Dunnhumby Retail Store Performance Analysis

> Part 1 of the Dunnhumby series. See [Part 2 — Retail Store Performance Analysis](https://github.com/ashishkumar-ds/data-science-projects/tree/main/dunnhumby-retail-performance-analysis) for the full analytical foundation.
> 

## Project Summary

This project analyzes **2.59M+ household-level transactions** from the Dunnhumby Retail Store dataset to drive a targeted intervention in underperforming stores. By combining **RFM customer segmentation**, **campaign ROI analysis**, and **time-of-day optimization**, the work delivers a prioritized, 60-day action plan projected to generate **≈$41K in incremental revenue**.

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
- **Households**: 103,200
- **Products**: 23,539
- **Time Frame**: 2017–2018  

---

## Key Findings

| Focus Area               | Insight                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Store Performance**    | Top 12% of stores (71) drive 80% of revenue; 511 are underperforming    |
| **Best Customers**       | Age 45–54, income $50K–$74K, no kids, 20.2% of base, 41% of revenue    |
| **Top Campaign**         | **Campaign 18**: 411.4% gross ROI, 278.7% net ROI    |
| **Optimal Timing**       | **Afternoon (12–18)** drives peak engagement and highest uplift         |
| **Forecast Impact**      | **30.1% sales uplift** projected across three validated pilot stores during the 56-day Campaign 18 period            |
---

## Recommendations

1. **Scale Campaign 18** to **85 eligible underperforming stores** (≥20 Best Customers)  
2. **Target Best Customers** — highest redemption (38%) and revenue contribution  
3. **Deploy exclusively in afternoon (12–18)** to capture peak response  
4. **Monitor via Tableau dashboard** to track uplift and adjust in real time  

> *Projected outcome: **≈$41K incremental revenue in 56 days** with 278.7% net ROI*

---

## Tools and Technologies

- **Python**: Pandas, Scikit-Learn, LightGBM, Optuna 
- **Visualization**: Matplotlib, Seaborn, Tableau  
- **Methods**: RFM Segmentation, ROI Analysis, Time-Series Forecasting  

---

## Project Structure

```bash
dunnhumby-retail-performance/
│
├── notebooks/                          # Data cleaning + store performance analysis
│   ├── data_cleaning.ipynb
│   └── store_performance_analysis.ipynb
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
