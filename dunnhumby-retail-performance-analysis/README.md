# Dunnhumby Retail Store Performance Analysis

## Project Summary

This project analyzes **2.59M+ household-level transactions** from the Dunnhumby Retail Store dataset to drive a targeted intervention in underperforming stores. By combining **RFM customer segmentation**, **campaign ROI analysis**, and **time-of-day optimization**, the work delivers a prioritized, 60-day action plan projected to generate **≈$15K in incremental revenue**.

An interactive **Tableau dashboard** enables real-time monitoring of store performance, customer segments, and campaign response, empowering managers to act on insights immediately.

---

## Problem Statement

- **88% of stores (511 of 582)** are underperforming, generating only **20% of total sales**  
- These stores show **monthly sales growth below 9.3%** (category average)

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
| **Store Performance**    | Top 12% of stores (69) drive 80% of revenue; 511 are underperforming    |
| **Best Customers**       | Age 45–54, income $50K–$74K, no kids, 20.2% of base, 41% of revenue    |
| **Top Campaign**         | **Campaign 18**: 411.4% gross ROI, 278.7% net ROI    |
| **Optimal Timing**       | **Afternoon (12–18)** drives peak engagement and highest uplift         |
| **Forecast Impact**      | **11% sales uplift** projected for Store #289 over 60 days              |

---

## Recommendations

1. **Scale Campaign 18** to **85 eligible underperforming stores** (≥20 Best Customers)  
2. **Target Best Customers** — highest redemption (38%) and revenue contribution  
3. **Deploy exclusively in afternoon (12–18)** to capture peak response  
4. **Monitor via Tableau dashboard** to track uplift and adjust in real time  

> *Projected outcome: **≈$15K incremental revenue in 60 days** with 278.7% net ROI*

---

## Tools and Technologies

- **Python**: pandas, LightGBM, Optuna, scikit-learn  
- **Visualization**: Tableau, Matplotlib, Seaborn  
- **Methods**: RFM Segmentation, ROI Analysis, Time-Series Forecasting  

---

## Project Structure

```bash
dunnhumby-retail-performance/
│
├── notebooks/        # Data cleaning + main analysis (with full business impact)
│   ├── data_cleaning.ipynb
│   └── main_analysis.ipynb
│
├── dashboard/        # Tableau dashboard for real-time store monitoring
│   └── dashboard_screenshot.png
│
├── presentation/     # Executive-ready deck for stakeholders
│   └── presentation_deck.pdf
│
└── README.md
