# Transforming Shopping Experience Through Market Basket Analysis

## Project Summary

This project explores customer purchasing behavior at Walmart using Market Basket Analysis. Faced with a 17% drop in sales in late 2015, the goal is to uncover hidden product associations and recommend bundling strategies, product placements, and personalized promotions to improve customer experience and boost sales.

---

## Problem Statement

Walmart observed a significant decline in sales in late 2015, raising concerns about customer satisfaction and in-store engagement.

**Business Question:**  
How can Walmart use product co-purchase patterns to create a more personalized shopping experience and increase average basket value?

---

## Dataset Description

- **Source**: Simulated Walmart Grocery Transactions  
- **Scope**: 38,008 transactions  
- **Time Frame**: 2014–2015  
- **Key Features**:
  - `Date`: Transaction date  
  - `Member_number`: Unique customer ID  
  - `itemDescription`: Product purchased  
- **Product Count**: 167 unique grocery items

---

## Key Findings

| Focus Area             | Insight                                                              |
|------------------------|----------------------------------------------------------------------|
| Product Popularity     | Milk, vegetables, and fruits were among the most frequently bought   |
| Underperforming Items  | Several items sold fewer than 10 units in 2 years                    |
| Product Associations   | Strong cross-sell relationships discovered using Apriori algorithm   |
| Timing Insight         | Transactions spiked during weekends and holidays                     |
| Customer Behavior      | Repeat customers frequently repurchased bundled grocery items        |

---

## Recommendations

1. Bundle top associated products into value packs to encourage higher basket size  
2. Reorganize store layout to place commonly paired products near each other  
3. Offer targeted promotions on low-selling items when purchased with top-sellers  
4. Use these insights to inform online and in-store merchandising strategies  

---

## Tools and Technologies

- Python 
- Market Basket Modeling: Apriori (via apyori)  
- Association Metrics: Support, Confidence, Lift   
- Tableau  

---

## Project Structure

```bash
walmart-market-basket-analysis/
│
├── notebooks/        # Apriori model, EDA, product pairings
│   └── Walmart_Market_Basket_Analysis.ipynb
│
├── dashboard/        # Tableau KPI dashboard for product performance simulation
│   └── dashboard_screenshot.png
│
├── presentation/     # Final business presentation for non-technical stakeholders
│   └── transforming_shopping_experience_presentation.pdf
│
├── data/             # Transaction dataset used for analysis
│   └── Walmart_Market_Basket_Groceries_dataset.csv
│
└── README.md

