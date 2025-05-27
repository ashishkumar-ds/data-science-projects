# Notebooks: Dunnhumby Retail Store Performance Analysis

This folder contains two Jupyter notebooks that document the complete workflow of the project — from raw data preparation to business insight generation.

---

## 1. `data_cleaning.ipynb`  
**Purpose:** Prepare and standardize the raw datasets from Dunnhumby for analysis.

### Cleaning Approach and Methodology

| Step                         | Column(s) / Table           | Issue / Reason                            | Before Example             | After Example              |
|------------------------------|-----------------------------|--------------------------------------------|----------------------------|----------------------------|
| Column Standardization       | All datasets                | Inconsistent casing and spacing            | `"Product Name"`           | `product_name`             |
| Missing Values               | `AGE_DESC`, `INCOME_DESC`   | Incomplete demographic records             | `NaN`                      | Row dropped                |
| Date Formatting              | `BASKET_DT`, `START_DT`, `END_DT` | Stored as strings, needed for filtering  | `"2018-01-15"`             | `2018-01-15` (datetime)    |
| Categorical Cleaning         | `AGE_DESC`, `INCOME_DESC`   | Inconsistent formats                       | `"45 - 54"`                | `"45-54"`                  |
| Data Merging                 | All datasets                | Needed a unified structure for modeling    | Multiple separate tables   | One consolidated dataframe |
| Feature Engineering          | Transactions + Campaigns    | Needed customer scores for segmentation    | No RFM scores              | `recency`, `frequency`, `monetary`, `rfm_score` created |

After cleaning, the data was ready for segmentation and campaign evaluation.

---

## 2. `main_analysis.ipynb`  
**Purpose:** Analyze store performance, customer segments, campaign effectiveness, and recommend actions.

### Analytical Workflow

- **Store Performance Evaluation**  
  - Identified underperforming stores using Pareto analysis  
  - Found that 96.6% of stores had <9.3% monthly sales growth  

- **Customer Segmentation (RFM)**  
  - Best Customers identified by high frequency and monetary, low recency  
  - Profile: Age 45–54, income $50K–$74K, two adults, no kids  

- **Campaign Performance Analysis**  
  - Assessed 30 campaigns using ROI and conversion metrics  
  - Campaign 18 was the most effective  
    - 10.8% revenue growth in 55 days  
    - 0.19% average daily sales growth  

- **Time-of-Day Sales Analysis**  
  - Afternoon campaigns led to the highest uplift:  
    - 17% growth  
    - 46% of total daily sales revenue  

- **Forecasting**  
  - Trend-based forecast for Store 289 shows 12.06% projected growth over 60 days  

---

## Summary

These notebooks together demonstrate a complete business analytics pipeline:

- `data_cleaning.ipynb`: Data transformation from raw to analysis-ready  
- `main_analysis.ipynb`: Insight generation, strategic recommendations, and forecasting  

This separation of concerns ensures a clear and reproducible project structure for stakeholders, reviewers, and future development.
