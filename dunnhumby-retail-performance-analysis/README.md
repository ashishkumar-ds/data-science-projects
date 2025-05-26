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

### 1. Data Collection and Understanding

Imported the Dunnhumby dataset consisting of over 2.5 million transaction records at the household level.

Key files loaded include:

- `hh_demographic.csv`: Household demographic data  
- `campaign_table.csv`: Campaign metadata  
- `coupon_redempt.csv`: Coupon redemption records  
- `campaign_desc.csv`: Campaign descriptions  
- `product.csv`: Product-level information  
- `transaction_data.csv`: Detailed purchase history  

---

### 2. Data Preprocessing and Cleaning (`data_cleaning.ipynb`)

This notebook focuses on preparing the dataset for analysis. Major steps:

#### a. Handling Missing Values

- Checked all files for nulls using `isnull().sum()`  
- Removed rows with excessive missing demographic fields  
- Verified missing values in non-critical fields did not affect segmentation or campaign analysis  

#### b. Standardizing Column Names

- Converted all column names to lowercase  
- Replaced spaces with underscores for consistency across joins and transformations  

#### c. Data Type Conversion

- Converted date strings to datetime format:  
  - `transaction_data["BASKET_DT"]` → datetime  
  - `campaign_table["START_DT"]`, `["END_DT"]` → datetime  

#### d. Merging Datasets

- Merged datasets on relevant keys such as:  
  - `household_key`  
  - `PRODUCT_ID`  
  - `CAMPAIGN`  
- Resulted in a unified dataframe for segmentation and campaign analysis  

#### e. Feature Engineering

- Created RFM (Recency, Frequency, Monetary) variables for each household:  
  - **Recency**: Days since last purchase  
  - **Frequency**: Number of transactions  
  - **Monetary**: Total spend  
- Assigned customer segments using quantiles of R, F, and M scores  

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
