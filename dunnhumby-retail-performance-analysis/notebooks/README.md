# Dunnhumby Retail Store Performance – Notebooks

This folder contains two Jupyter notebooks that document the complete analytical workflow for improving sales across underperforming stores using customer-level transaction data. The analysis focuses on segmentation, campaign evaluation, and revenue forecasting.

---

## Methodology

### 1. Data Cleaning & Preparation (`data_cleaning.ipynb`)

| Step                  | Column(s)         | Before                          | After                              |
|-----------------------|-------------------|----------------------------------|------------------------------------|
| Dataset merging       | Multiple files    | Separate tables for campaigns, coupons, products, etc. | Merged into a master dataset     |
| Data type formatting  | `household_key`   | Integer                          | Converted to string                |
| Feature creation      | `DAY`             | Raw day values                   | Derived `month_no`, `day_no`       |
| Column renaming       | `BASKET_ID`       | Original column name             | Renamed to `TOTAL_BASKET`          |
| Dropping columns      | `RETAIL_DISC`     | Present in raw data              | Removed as non-essential           |

After cleaning and transformation, the data was ready for customer segmentation and campaign performance evaluation.

---

### 2. Business Analysis & Modeling (`main_analysis.ipynb`)

- **Store Performance Evaluation**:
  - Conducted Pareto analysis: Found that 12% of stores drive 80% of revenue
  - Labeled 96.6% of stores as underperforming based on monthly sales growth < 9.3%

- **Customer Segmentation (RFM)**:
  - Applied RFM scoring based on Recency, Frequency, and Monetary value
  - Identified “Best Customers” profile:
    - Age: 45–54
    - Income: $50K–$74K
    - Household: Two adults with no children

- **Campaign Effectiveness**:
  - Analyzed 30 campaigns using Conversion Rate, Coupon Redemption, and ROI
  - Campaign 18 was the most successful:
    - 10.8% increase in revenue over 55 days
    - 0.19% uplift in daily sales

- **Time-of-Day Sales Analysis**:
  - Found afternoon campaigns performed best:
    - 17% revenue uplift
    - 46% of total daily sales volume

- **Forecasting**:
  - Used linear trend projection to forecast the impact of applying recommendations
  - Estimated 12.06% increase in store revenue over 60 days

---

## Key Outputs

- Cleaned and integrated retail dataset from six sources  
- RFM segments for customer targeting  
- Campaign performance rankings and uplift calculations  
- Forecast model for revenue projection

---

## Business Insight Integration

The customer segmentation, campaign evaluation, and store performance insights generated from this notebook were applied in:

- **[Presentation Deck](../presentation/dunnhumby_retail_performance_analysis_presentation_deck.pdf)**  

- **[Interactive Tableau Dashboard](../dashboard/dashboard_screenshot.png)**
