# Driving Retail Store Performance Through Customer Analytics and Targeted Campaigns

## Project Summary

This project analyzes over 2.5 million household-level transactions from Dunnhumby to uncover data-driven strategies that improve sales in underperforming retail stores. By combining customer segmentation (RFM analysis), campaign effectiveness evaluation, and time-based engagement insights, the analysis identifies actionable recommendations to target the right customers with the right campaigns at the right time.

To support decision-makers, an interactive Tableau dashboard was also developed to help store managers track performance, compare regions, and monitor the real-time impact of the implemented strategies

---

## Problem Statement

Only 12% of stores account for 80% of total revenue. The remaining 96.6% are underperforming with monthly sales growth below 9.3%.


**Business Question:**  
How can Dunnhumby increase the sales value of underperforming stores within a two-month period through better targeting and campaign strategies?

---

## Dataset Description

- **Source**: Dunnhumby 
- **Scope**: 2,500,000 transaction records  
- **Time Frame**: 2017–2018  
- **Key Features**:
  - Customer demographics  
  - Transaction time  
  - Product information  
  - Campaign and coupon data  
  - Store identifiers  

---

## Key Findings

| Focus Area               | Insight                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| Store Sales Distribution | 96.6% of stores show below-average monthly sales growth                 |
| Customer Segment         | Best Customers are aged 45–54, income $50K–$74K, typically no children  |
| Campaign Effectiveness   | Campaign 18 outperformed others in ROI and engagement                   |
| Time of Engagement       | Afternoon is the most profitable time slot post-campaign                |
| Forecast Impact          | Predicted 12.06% sales increase over 60 days in targeted stores         |

---

## Recommendations

1. Prioritize Campaign 18 for stores identified as underperforming  
2. Target the Best Customer segment to maximize campaign effectiveness  
3. Schedule campaigns in the afternoon to leverage peak engagement and conversion  
4. Monitor uplift and performance using forecasting models to refine strategies  

---

## Tools and Technologies

- Python: Pandas, NumPy, Matplotlib, Seaborn  
- Tableau  
- RFM Segmentation  
- ROI and Campaign Analytics  
- Trend-Based Forecasting  

---

## Project Structure

```bash
dunnhumby-retail-performance/
│
├── notebooks/        # Data cleaning, segmentation, campaign analysis, forecasting
│   ├── data_cleaning.ipynb
│   └── main_analysis.ipynb
│
├── dashboard/        # Tableau dashboard files for store performance tracking
│   ├── dunnhumby_dashboard.twbx
│   └── dashboard_screenshot.png
│
├── presentation/     # Final business presentation for non-technical stakeholders
│   └── dunnhumby_retail_performance_analysis_presentation_deck.pdf
│
└── README.md  
