# Driving Retail Store Performance Through Customer Analytics and Targeted Campaigns

## Project Summary

This project explores store-level transaction data from Dunnhumby, a global customer data science company. By identifying underperforming stores and analyzing customer behavior, the analysis reveals data-driven strategies to increase sales. Through RFM-based segmentation, campaign effectiveness analysis, and time-based targeting, the project recommends using Campaign 18 to reach the Best Customer segment during high-engagement time slots, with the goal of boosting revenue in underperforming stores.

---

## Problem Statement

Approximately 80% of the total sales come from just 12% of stores. The remaining 96.6% of stores are considered underperforming, with monthly sales growth below the company average of 9.3%.

**Business Question:**  
How can Dunnhumby increase the sales value of underperforming stores within a two-month period through better targeting and campaign strategies?

---

## Dataset Description

- **Source**: Dunnhumby (via Kaggle)  
- **Scope**: 2,500,000 transaction records  
- **Time Frame**: 2017–2018  
- **Key Features**:
  - Customer demographics  
  - Transaction time  
  - Product information  
  - Campaign and coupon data  
  - Store identifiers  

---

## Approach and Methodology

### 1. Store Performance Analysis
- Applied Pareto analysis to determine that 12% of stores generate 80% of sales.
- Identified 96.6% of stores as underperforming due to sub-9.3% monthly growth.

### 2. Customer Segmentation using RFM Model
- Segmented customers based on Recency, Frequency, and Monetary values.
- Identified "Best Customers" as those with:
  - Lowest recency (recent transactions)
  - Highest frequency (repeat purchases)
  - Highest monetary value (total spend)

### 3. Campaign Analysis
- Evaluated 30 promotional campaigns using conversion rate, ROI, and product engagement metrics.
- Campaign 18 emerged as the most effective:
  - 486.6% total performance score
  - 10.8% revenue increase during the 55-day campaign
  - 0.19% average daily sales growth

### 4. Time-Based Campaign Targeting
- Analyzed the timing of sales before and after Campaign 18.
- Afternoon campaigns led to:
  - 17% growth in average sales
  - 46% share of daily sales volume

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

1. Prioritize Campaign 18 for stores identified as underperforming.  
2. Target the Best Customer segment to maximize campaign effectiveness.  
3. Schedule campaigns in the afternoon to leverage peak engagement and conversion.  
4. Monitor uplift and performance using forecasting models to refine strategies.

---

## Tools and Technologies

- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- Tableau
- RFM Segmentation  
- ROI and Campaign Analytics  
- Trend-Based Forecasting  
