# Walmart Market Basket Analysis – Apriori Algorithm

This notebook analyzes synthetic grocery transaction data designed to reflect customer shopping patterns at Walmart. Using Market Basket Analysis and the Apriori algorithm, it identifies frequently bought-together items and provides insights to support bundling strategies, product placement, and promotion planning.

---

## Methodology

### 1. Data Generation

- The dataset used in this project is **synthetic** and was generated using **ChatGPT** to simulate realistic Walmart grocery transactions.
- It includes over 38,000 transactions from 2014–2015, with three columns: `Date`, `Member_number`, and `itemDescription`.

---

### 2. Data Cleaning & Preparation

| Step                  | Column(s)           | Before                                   | After                                 |
|-----------------------|---------------------|-------------------------------------------|----------------------------------------|
| Duplicate removal     | Entire dataset      | 76 duplicate rows                         | Duplicates removed                     |
| Data type conversion  | `Date`              | String format                             | Converted to `datetime`                |
|                       | `Member_number`     | Integer                                   | Converted to string for grouping       |
| Text formatting       | `Item_description`  | Inconsistent casing, extra spaces         | Cleaned and standardized               |
| Transaction reshaping | Customer-item pairs | Individual product rows per transaction   | Grouped into item lists per customer   |

The data was cleaned, standardized, and reshaped into transaction lists suitable for association rule mining.

---

### 3. Exploratory Data Analysis (EDA)

- Identified high-frequency items (e.g., Milk, Vegetables, Fruits, RTE Foods)
- Detected multiple underperforming items (e.g., Pancake Syrup, BBQ Sauce, Mango Chutney)
- Visualized:
  - Top 5 most sold items
  - Monthly sales patterns and seasonality

---

### 4. Feature Engineering

- Grouped purchases by `Member_number` to simulate individual shopping baskets
- Transformed the data into the required format for the Apriori algorithm (`List[List[str]]`)

---

### 5. Modeling

- Applied the **Apriori algorithm** using the `apyori` package to identify frequent itemsets and strong product associations  
- Chose parameter values based on dataset size and business context:
  - `min_support = 0.002` – to capture commonly bought-together items  
  - `min_confidence = 0.05` – to ensure reliability of recommendations  
  - `min_lift = 3` – to prioritize high-impact rules  
  - `min_length = 2`, `max_length = 2` – to focus on product pairings  
- Generated a ranked list of associated product pairs with high support, confidence, and lift  
- These associations informed bundling, cross-sell opportunities, and product placement strategies  

---

### 6. Post-Processing

- Parsed Apriori rules into a readable DataFrame
- Extracted paired item rules and sorted them by lift and confidence
- Prepared the rule output for downstream recommendations

---

## Key Outputs

- Visuals highlighting product popularity and sales trends
- Cleaned transaction list used for modeling
- Ranked list of high-confidence item pairs, such as:
  - Potato Products & Beef (Confidence: 45%, Lift: 4.1)
  - Flour & Mayonnaise
  - Canned Fruit & Coffee
    
## Business Insight Integration

The association rules and product pairing insights generated from this notebook were applied in:

- **[Presentation Deck](../presentation/transforming_shopping_experience_presentation.pdf)**
