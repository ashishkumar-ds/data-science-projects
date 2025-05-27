# Notebooks: Dunnhumby Retail Store Performance Analysis

This folder contains two Jupyter notebooks that document the full analytics workflow — from raw data to business recommendations — for improving retail store performance using customer segmentation and campaign data.

---

## Notebook Overview

### 1. `data_cleaning.ipynb`  
**Purpose:** Transform raw datasets into a clean, analysis-ready format by resolving data quality issues and engineering features for segmentation.

### 2. `main_analysis.ipynb`  
**Purpose:** Perform business analysis using the cleaned dataset to uncover insights, evaluate marketing campaigns, and forecast potential revenue uplift.

---

## Data Preparation Summary (`data_cleaning.ipynb`)

The following issues were addressed to prepare the dataset:

| Task                        | Why It Was Needed                                     | Before Example             | After Example              |
|-----------------------------|-------------------------------------------------------|----------------------------|----------------------------|
| **Column renaming**         | Ensure consistency and ease of use                    | `"Product Name"`           | `product_name`             |
| **Handling missing values** | Clean incomplete demographic records                  | `NaN` in `AGE_DESC`        | Dropped 90 rows            |
| **Date formatting**         | Enable time-based filtering and recency calculation   | `"2018-01-15"` (string)    | `2018-01-15` (datetime)    |
| **Standardizing categories**| Remove inconsistent formatting                        | `"45 - 54"`                | `"45-54"`                  |
| **Data merging**            | Create a unified view across households, products, and campaigns | Separate files | Consolidated master dataframe |
| **Feature engineering**     | Create RFM metrics for segmentation                   | Raw transaction totals     | `recency`, `frequency`, `monetary`, `rfm_score` |

> 📌 Result: A consolidated dataset with household-level RFM scores, campaign metadata, and product info, ready for analysis.

---

## Analysis Workflow Summary (`main_analysis.ipynb`)

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
- Trend-based forecast showed a **12.06% projected uplift** over 60 days for Store 289 if the recommendations are applied.

---

## Summary

These two notebooks together deliver a full project pipeline:

- `data_cleaning.ipynb`:  
  - Transforms raw, fragmented datasets into a structured and enriched format  
  - Prepares features that fuel meaningful segmentation  

- `main_analysis.ipynb`:  
  - Leverages that structure to uncover deep customer and campaign insights  
  - Offers data-backed strategies to drive sales growth in underperforming stores  

This modular approach makes the project easy to understand, scalable, and reusable across similar business problems.
