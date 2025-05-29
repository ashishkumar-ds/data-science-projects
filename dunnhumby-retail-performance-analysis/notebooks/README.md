# Notebooks: Dunnhumby Retail Store Performance Analysis

This folder contains two Jupyter notebooks that document the complete workflow of the project - from raw data preparation to business insight generation.


---

## Notebook Overview

### 1. Data Preparation [`data_cleaning.ipynb`](https://github.com/ashishkumar-ds/data-science-projects/blob/main/dunnhumby-retail-performance-analysis/notebooks/data%20cleaning.ipynb) 
**Purpose:** Transform raw datasets into a clean, analysis-ready format by resolving data quality issues and engineering features for segmentation.

### 2. Data Analysis [`main_analysis.ipynb`](https://github.com/ashishkumar-ds/data-science-projects/blob/main/dunnhumby-retail-performance-analysis/notebooks/main%20analysis.ipynb) 
**Purpose:** Perform business analysis using the cleaned dataset to uncover insights, evaluate marketing campaigns, and forecast potential revenue uplift.

---

## Data Preparation Summary 

This notebook focuses on preparing the data for analysis by merging raw tables, fixing inconsistencies, and engineering helpful features.

### What Was Done

- Combined multiple datasets: products, campaigns, coupons, transactions, and households
- Converted data types (e.g., `household_key` from integer to string)
- Created two new features from the `DAY` field:  
  - `month_no`: to group transactions by month  
  - `day_no`: to understand day-of-week trends  
- Renamed columns for consistency (e.g., `BASKET_ID` → `TOTAL_BASKET`)
- Removed unnecessary fields like `RETAIL_DISC`

### Before vs After

| Step                  | Column(s)         | Before                          | After                              |
|-----------------------|-------------------|----------------------------------|------------------------------------|
| Merging datasets      | All major tables  | Separate files                  | Combined into a master dataset     |
| Data type formatting  | `household_key`   | Integer                          | String                             |
| Feature creation      | `DAY`             | Raw day value                    | Added `month_no`, `day_no`         |
| Column renaming       | `BASKET_ID`       | `BASKET_ID`                      | `TOTAL_BASKET`                     |
| Dropping columns      | `RETAIL_DISC`     | Present                          | Removed                            |


After cleaning, the data was ready for segmentation and campaign evaluation.

---

## Analysis Workflow Summary

This notebook applies analytics to drive business insights and recommendations:

### 1. Store Performance Evaluation
- Used Pareto analysis to show that **12% of stores generate 80% of revenue**
- Identified **96.6% of stores as underperforming** (monthly growth < 9.3%)

### 2. Customer Segmentation (RFM)
- Grouped customers by Recency, Frequency, and Monetary value
- Highlighted **Best Customers** with high spend and frequent visits:
  - Age: 45–54  
  - Income: $50K–$74K  
  - Household: Two adults, no kids

### 3. Campaign Effectiveness Analysis
- Compared **30 campaigns** by:
  - Conversion Rate
  - Coupon Redemption
  - ROI
- **Campaign 18** stood out:
  - Drove **10.8% revenue growth** over 55 days
  - Increased daily sales by 0.19%

### 4. Time-of-Day Sales Analysis
- Afternoon campaigns produced:
  - **17% uplift**
  - **46% of total daily revenue**

### 5. Forecasting Sales Impact
- Used **linear trend projection** to estimate impact on a test store.
- Predicted **12.06% sales growth** over 60 days if recommendations are applied.
