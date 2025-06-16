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

Great! Here's the updated version of your **Key Findings** and **Recommendations**:

* ✅ Named the underperforming products based on the PDF
* ✅ Removed all arrow signs (→)

---

## Key Findings

| Focus Area            | Insight                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Product Popularity    | Milk, vegetables, fruits, and RTE (ready-to-eat) foods were among the most frequently purchased items                    |
| Underperforming Items | Products like Pancake Syrup, Tuna Salad, BBQ Sauce, and Mango Chutney sold fewer than 8 units over 2 years               |
| Product Associations  | Strong cross-sell relationships discovered using Apriori, including Potato Products with Beef, and Flour with Mayonnaise |
| Cross-Sell Confidence | Over 40% confidence in item pairs like Canned Fruit with Coffee, and Meat Spreads with Eggs                              |
| Timing Insight        | Transaction volumes spiked during weekends and holidays                                                                  |
| Customer Behavior     | Repeat customers frequently repurchased bundled grocery essentials, showing loyalty-driven buying patterns               |

---

## Recommendations

1. **Bundle frequently associated products** (e.g., Potato Products with Beef, Flour with Mayonnaise) to increase basket size
2. **Place cross-sell items near each other** on shelves to boost impulse purchases
3. **Promote underperforming items** (e.g., BBQ Sauce, Tuna Salad) when bought with popular products
4. **Schedule campaigns during high-traffic times** like weekends and holidays for better response
5. **Personalize promotions** using co-purchase insights through apps, receipts, or in-store signage

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

