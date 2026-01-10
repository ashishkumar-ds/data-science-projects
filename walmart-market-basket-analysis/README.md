# Walmart Grocery Market Basket Analysis

## Project Summary

This project analyzes **38,000+ grocery transactions** from a synthetic **Walmart grocery dataset** to uncover hidden product affinities and optimize merchandising strategies. By applying **Market Basket Analysis** using the **FP-Growth algorithm**, the work identifies high-confidence product pairings such as **Potato Products + Beef** and **Flour + Mayonnaise**, enabling targeted promotions and strategic shelf placement.

The insights drive actionable recommendations projected to increase **average basket size by 24.8%** and generate an estimated **$23.5K in annual incremental revenue** through intelligent bundling and cross-selling.

An interactive **Looker Studio dashboard** visualizes key association rules, temporal shopping patterns, and revenue impact projections for ongoing performance monitoring.

---

## Problem Statement

- Walmart experienced a **17% sales decline** in late 2015  
- Customer engagement and basket value require immediate improvement  

**Business Question**:  
> How can Walmart leverage purchase pattern insights to improve product placement, create targeted promotions, and deliver a better shopping experience—ultimately increasing basket size and reversing sales decline?

---

## Dataset Description

- **Source**: Synthetic Walmart grocery transaction data (2014–2015)  
- **Time Frame**: 2 years (2014–2015)  
- **Total Transactions**: 38,006  
- **Unique Products**: 167 across diverse categories (fresh produce, dairy, household, etc.)  
- **Customers**: 3,898 unique member numbers  

### Key Features:
- **Product-level granularity**: Includes items like *Whole Milk*, *Other Vegetables*, *Soda*  
- **Temporal data**: Full date stamps enabling day-of-week and monthly trend analysis  
- **Realistic distribution**: Mirrors actual grocery purchasing behavior  

---

## Key Findings

| Focus Area               | Insight                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Top-Selling Items**    | **Whole Milk**, **Other Vegetables**, **Rolls/Buns** dominate baskets (40%+ of transactions) |
| **High-Lift Pairs**      | **Potato Products + Beef** (Lift: 3.8x), **Kitchen Towels + UHT Milk** (Lift: 3.8x) |
| **Peak Shopping Times**  | **Wednesdays & Thursdays** show highest traffic; **August** has seasonal demand spike |
| **Underperforming Items**| **Makeup Remover**, **Kitchen Utensil**, **Preservation Products** lag significantly |
| **Projected Impact**     | **24.8% basket size increase**, **$2K/month ($23.5K/year) incremental revenue** |

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

- **Python**: pandas, mlxtend (FP-Growth), Matplotlib, Seaborn  
- **Visualization**: Looker Studio (dashboard), WordCloud  
- **Methods**: Market Basket Analysis, FP-Growth Algorithm, Lift/Confidence Metrics  

---

## Project Structure

```bash
walmart-grocery-market-basket/
│
├── notebooks/              # Complete analysis with statistical validation
│   └── Grocery-Market-Basket-Analysis.ipynb
│
├── dashboard/              # Interactive Looker Studio dashboard
│   └── walmart_basket_analysis_dashboard.pdf
│
├── presentation/           # Executive summary deck
│   └── Grocery_Market_Basket_Analysis_Presentation.pdf
│
└── README.md
```# Walmart Grocery Market Basket Analysis

## Project Summary

This project analyzes **38,000+ grocery transactions** from a synthetic **Walmart grocery dataset** to uncover hidden product affinities and optimize merchandising strategies. By applying **Market Basket Analysis** using the **FP-Growth algorithm**, the work identifies high-confidence product pairings such as **Potato Products + Beef** and **Flour + Mayonnaise**, enabling targeted promotions and strategic shelf placement.

The insights drive actionable recommendations projected to increase **average basket size by 24.8%** and generate an estimated **$23.5K in annual incremental revenue** through intelligent bundling and cross-selling.

An interactive **Looker Studio dashboard** visualizes key association rules, temporal shopping patterns, and revenue impact projections for ongoing performance monitoring.

---

## Problem Statement

- Walmart experienced a **17% sales decline** in late 2015  
- Customer engagement and basket value require immediate improvement  

**Business Question**:  
> How can Walmart leverage purchase pattern insights to improve product placement, create targeted promotions, and deliver a better shopping experience—ultimately increasing basket size and reversing sales decline?

---

## Dataset Description

- **Source**: Synthetic Walmart grocery transaction data (2014–2015)  
- **Time Frame**: 2 years (2014–2015)  
- **Total Transactions**: 38,006  
- **Unique Products**: 167 across diverse categories (fresh produce, dairy, household, etc.)  
- **Customers**: 3,898 unique member numbers  

### Key Features:
- **Product-level granularity**: Includes items like *Whole Milk*, *Other Vegetables*, *Soda*  
- **Temporal data**: Full date stamps enabling day-of-week and monthly trend analysis  
- **Realistic distribution**: Mirrors actual grocery purchasing behavior  

---

## Key Findings

| Focus Area               | Insight                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Top-Selling Items**    | **Whole Milk**, **Other Vegetables**, **Rolls/Buns** dominate baskets (40%+ of transactions) |
| **High-Lift Pairs**      | **Potato Products + Beef** (Lift: 3.8x), **Kitchen Towels + UHT Milk** (Lift: 3.8x) |
| **Peak Shopping Times**  | **Wednesdays & Thursdays** show highest traffic; **August** has seasonal demand spike |
| **Underperforming Items**| **Makeup Remover**, **Kitchen Utensil**, **Preservation Products** lag significantly |
| **Projected Impact**     | **24.8% basket size increase**, **$2K/month ($23.5K/year) incremental revenue** |

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

- **Python**: pandas, mlxtend (FP-Growth), Matplotlib, Seaborn  
- **Visualization**: Tableau  
- **Methods**: Market Basket Analysis, FP-Growth Algorithm, Lift/Confidence Metrics  

---

## Project Structure

```bash
walmart-grocery-market-basket/
│
├── notebooks/              # Complete analysis with statistical validation
│   └── Grocery-Market-Basket-Analysis.ipynb
│
├── dashboard/              # Interactive Looker Studio dashboard
│   └── walmart_basket_analysis_dashboard.pdf
│
├── presentation/           # Executive summary deck
│   └── Grocery_Market_Basket_Analysis_Presentation.pdf
│
└── README.md
```