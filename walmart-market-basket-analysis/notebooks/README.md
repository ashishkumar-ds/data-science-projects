# Walmart Market Basket Analysis

This notebook analyzes historical transaction data from a simulated Walmart grocery dataset to uncover meaningful product associations. Using Market Basket Analysis and the Apriori algorithm, it identifies frequently bought-together items and provides insights to support bundling strategies, product placement, and promotion planning.

---

## Methodology

### 1. Data Cleaning & Preparation

| Step                  | Column(s)           | Before                                   | After                                 |
|-----------------------|---------------------|-------------------------------------------|----------------------------------------|
| Duplicate removal     | Entire dataset      | 76 duplicate rows                         | Duplicates removed                     |
| Data type conversion  | `Date`              | String format                             | Converted to `datetime`                |
|                       | `Member_number`     | Integer                                   | Converted to string for grouping       |
| Text formatting       | `Item_description`  | Inconsistent casing, extra spaces         | Cleaned and standardized               |
| Transaction reshaping | Customer-item pairs | Individual product rows per transaction   | Grouped into item lists per customer   |

The data was cleaned, standardized, and reshaped into transaction lists suitable for association rule mining.

---

### 2. Exploratory Data Analysis (EDA)

- Identified high-frequency items (e.g., Milk, Vegetables, Fruits, RTE Foods)
- Detected multiple underperforming items (e.g., Pancake Syrup, BBQ Sauce, Mango Chutney)
- Visualized:
  - Top 5 most sold items
  - Monthly sales patterns and seasonality

---

### 3. Feature Engineering

- Grouped purchases by `Member_number` to simulate individual shopping baskets
- Transformed the data into the required format for the Apriori algorithm

---

### 4. Modeling 

- **Algorithm Used**: Apriori (`apyori` package)
- **Parameters**:
  - `min_support = 0.002`
  - `min_confidence = 0.05`
  - `min_lift = 3`
  - `min_length = 2`, `max_length = 2`
- Output: Frequent itemsets and strong association rules based on support, confidence, and lift

---

### 5. Post-Processing

- Parsed Apriori rules into a readable DataFrame
- Extracted paired item rules and sorted them by lift and confidence
- Prepared the rule output for downstream recommendations

---

## Key Outputs

- Ranked list of high-confidence item pairs, such as:
  - Potato Products & Beef (Confidence: 45%, Lift: 4.1)
  - Flour & Mayonnaise
  - Canned Fruit & Coffee
- Visuals highlighting product popularity and sales trends
- Cleaned transaction list used for modeling
- Business-ready insights used in:
  - 📄 [Presentation deck](../presentation/transforming_shopping_experience_presentation.pdf)
  - 📊 [KPI dashboard](../dashboard/dashboard_screenshot.png)
