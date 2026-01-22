# Walmart Grocery Market Basket Analysis

## Project Summary

This project analyzes **38,000+ grocery transactions** from a synthetic **Walmart grocery dataset** to boost basket value through strategic product bundling and placement. By combining **Market Basket Analysis**, **high-lift association rules**, and **temporal shopping patterns**, the work delivers an actionable plan projected to generate **≈$2K in annual incremental revenue**($23.5K annually). 

---

## Problem Statement

- Walmart experienced a **32% sales decline** in late 2015  
- Customer engagement and basket value require immediate improvement  

**Business Question**:  
> How can Walmart leverage purchase pattern insights to improve product placement, create targeted promotions, and deliver a better shopping experience ultimately increasing basket size and reversing sales decline?

---

## Dataset Description

- **Source**: [Synthetic Walmart grocery transaction data](https://github.com/ashishkumar-ds/data-science-projects/blob/main/walmart-market-basket-analysis%2Fdataset%2Fgroceries%20dataset.xlsx)
- **Total Transactions**: 38,006  
- **Customers**: 3,898 unique member numbers  
- **Unique Products**: 167 across diverse categories (fresh produce, dairy, household, etc.)
- **Time Frame**: 2 years (2014–2015)  

---

## Key Findings

| Focus Area               | Insight                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Top-Selling Items**    | **Whole Milk**, **Other Vegetables**, **Rolls/Buns** dominate baskets (40%+ of transactions) |
| **High-Lift Pairs**      | **Potato Products + Beef** (Lift: 3.8x), **Kitchen Towels + UHT Milk** (Lift: 3.8x) |
| **Peak Shopping Times**  | **Wednesdays & Thursdays** show highest traffic; **August** has seasonal demand spike |
| **Underperforming Items**| **Makeup Remover**, **Kitchen Utensil**, **Preservation Products** lag significantly |

---

## Recommendations

1. **Implement Strategic Bundling**  
   - Create combo deals for high-lift pairs (*e.g., Potato Products + Beef*)  
   - Offer discounts when both items are purchased together  

2. **Optimize Shelf Placement**  
   - Position co-purchased items adjacently (*e.g., Flour next to Mayonnaise*)  
   - Place underperforming items near top sellers to drive discovery  

3. **Deploy Time-Based Promotions**  
   - Run targeted campaigns on **Wednesdays/Thursdays** during peak traffic  
   - Launch August-specific bundles capitalizing on seasonal spikes  

4. **Revitalize Low-Performers**  
   - Bundle **Makeup Remover** with complementary health/beauty products  
   - Feature **Kitchen Utensils** in cooking-themed displays with Flour/Mayonnaise  

> *Projected outcome: **24.8% larger baskets** and **$23.5K annual revenue uplift** through 10% bundling adoption*

---

## Tools and Technologies

- **Python**: pandas, mlxtend, Matplotlib, Seaborn  
- **Visualization**: Tableau
- **Data Generation**: ChatGPT
- **Methods**: Market Basket Analysis, FP-Growth Algorithm, Lift/Confidence Metrics  

---

```bash
walmart-grocery-market-basket/
│
├── notebooks/
│   └── market-basket-analysis.ipynb      # End-to-end analysis: FP-Growth, rule extraction, and insight generation
│
├── dashboard/
│   ├── dashboard_screenshot.png                  # Preview of the Tableau KPI dashboard
│   └── README.md                                 # Notes on dashboard design and simulation logic
│
├── presentation/
│   └── presentation_deck.pdf  # Executive slide deck for business stakeholders
│
└── README.md                                  
