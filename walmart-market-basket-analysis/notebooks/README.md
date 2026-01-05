This folder contains a notebook that walks through the end-to-end Walmart grocery market basket analysis workflow from data cleaning and exploratory analysis to association rule mining, product pairing discovery, and actionable merchandising strategy development.

---

## Main Analysis Notebook  
**File:**`notebooks/walmart_grocery_market_basket_analysis_.ipynb`

### Objective  
Discover strong product associations, analyze shopping behavior, and generate data-driven recommendations to increase basket size and revenue in Walmart grocery.

---

## 1. Data Understanding

| Data Source       | Rows     | Key Fields                          |
|-------------------|----------|-------------------------------------|
| Transaction       | 38,006   | `Member_number`, `Date`, `Item_description` |

> **Note**: Synthetic dataset designed to reflect realistic Walmart grocery behavior over 2 years (2014–2015), covering **167 unique products**.

---

## 2. Data Preparation

| Step                  | Action                                  | Outcome                          |
|-----------------------|-----------------------------------------|----------------------------------|
| Duplicate removal     | Checked for full-row duplicates         | None found                       |
| Data type conversion  | `Date` → datetime                       | Enabled time-based analysis      |
| Text standardization  | Unified casing and spacing (e.g., “milk” → “Whole Milk”) | Consistent product labels |
| Basket construction   | Grouped items by (`Member_number`, `Date`) | **14,963 unique shopping baskets** |


---

## 3. Exploratory Data Analysis

### 3.1 Product Popularity

| Category             | Top 5 Items                 | Bottom 5 Items               |
|----------------------|-----------------------------|-------------------------------|
| **Bestsellers**      | Whole Milk (2,363)          | Kitchen Utensil (1)           |
|                      | Other Vegetables (1,827)    | Bags (4)                      |
|                      | Rolls/Buns (1,646)          | Baby Cosmetics (3)            |
|                      | Soda (1,453)                | Toilet Cleaner (5)            |
|                      | Yogurt (1,285)              | Preservation Products (1)     |

**Key Insight:**  
Staples dominate baskets - top 5 items drive over **40% of transactions**. Underperforming items rarely appear in baskets and need strategic pairing.

### 3.2 Temporal Shopping Patterns

| Dimension    | Peak Period       | Insight                     |
|--------------|-------------------|-----------------------------|
| Weekday      | Wednesday–Thursday| ~25% of weekly transactions |
| Month        | August            | Highest monthly demand      |

**Key Insight:**  
**Midweek (Wed–Thu)** and **August** are optimal for promotions, staffing, and campaign launches.

---

## 4. Market Basket Analysis (FP-Growth)

| Rule                          | Support | Confidence | Lift  |
|-------------------------------|---------|------------|-------|
| Potato Products → Beef        | 0.0045  | 45%        | 3.8x  |
| Kitchen Towels → UHT Milk     | 0.0030  | 30%        | 3.8x  |
| Flour → Mayonnaise            | 0.0023  | 23%        | 3.3x  |

> **Thresholds**: `min_support = 0.002`, `min_confidence = 0.15`, `min_lift = 3.0`  
> **Validation**: Chi-squared test confirms statistical significance (**p < 0.05**)

**Key Insight:**  
High-lift rules reveal **meal-pairing** (Beef + Potatoes) and **household combos** (Towels + Milk), ideal for bundling and cross-merchandising.

---

## 5. Strategic Recommendations

- **Bundle high-lift pairs**: Launch *“Potato + Beef”* or *“Flour + Mayonnaise”* combo deals  
- **Optimize shelf layout**: Place co-purchased items adjacent to drive impulse buys  
- **Time promotions strategically**: Focus on **Wed–Thu** and **August**  
- **Leverage digital channels**: Deliver personalized offers via app, email, or receipts  

---

## 6. Business Impact

- **+24.8%** projected increase in average basket size (**2.54 → 3.17** items)  
- **$1,959** estimated **monthly revenue lift**  
- **$23,504** estimated **annual revenue lift**  

> **Assumptions**:  
> - 10% customer adoption of bundling offers  
> - $5.00 average item price  
> - Average lift from top 5 rules = **3.27x**

---

**Stack:** Python 3.9 · pandas · matplotlib · seaborn · mlxtend 