# Etsy Funnel Analysis - Notebooks

This folder contains the SQL queries used to analyze Etsy’s customer journey across its 8-stage e-commerce funnel. The goal was to uncover funnel performance gaps, monitor user progression, and calculate abandonment or conversion metrics that inform strategic improvements.

---

## Business Questions 

### 1. **How many users reach each funnel stage? (Funnel Counts - 2019 to 2022)** 

```sql
SELECT
  EXTRACT(YEAR FROM timestamp) AS year,
  EXTRACT(QUARTER FROM timestamp) AS quarter,

  COUNT(DISTINCT CASE WHEN event = 'productview' THEN user_id END) AS productview_count,
  COUNT(DISTINCT CASE WHEN event = 'addtocart' THEN user_id END) AS addtocart_count,
  COUNT(DISTINCT CASE WHEN event = 'viewcart' THEN user_id END) AS viewcart_count,
  COUNT(DISTINCT CASE WHEN event = 'chooseaddress' THEN user_id END) AS chooseaddress_count,
  COUNT(DISTINCT CASE WHEN event = 'choosedelivery' THEN user_id END) AS choosedelivery_count,
  COUNT(DISTINCT CASE WHEN event = 'changepaymentmethod' THEN user_id END) AS changepayment_count,
  COUNT(DISTINCT CASE WHEN event = 'checkout' THEN user_id END) AS checkout_count,
  COUNT(DISTINCT CASE WHEN event = 'complete' THEN user_id END) AS complete_count

FROM `etsy-funnel-analysis.etsyecommerce.events`
WHERE EXTRACT(YEAR FROM timestamp) BETWEEN 2019 AND 2022
GROUP BY year, quarter
ORDER BY year, quarter;
```

### 2. **What are the conversion rates between funnel stages? (Coversion Rates)** 

```sql
Conversion Rates (Calculated using Funnel Counts from Query 1)
WITH funnel_counts AS (
  SELECT
    EXTRACT(YEAR FROM timestamp) AS year,
    EXTRACT(QUARTER FROM timestamp) AS quarter,
    
    COUNT(DISTINCT CASE WHEN event = 'productview' THEN user_id END) AS productview_count,
    COUNT(DISTINCT CASE WHEN event = 'addtocart' THEN user_id END) AS addtocart_count,
    COUNT(DISTINCT CASE WHEN event = 'viewcart' THEN user_id END) AS viewcart_count,
    COUNT(DISTINCT CASE WHEN event = 'chooseaddress' THEN user_id END) AS chooseaddress_count,
    COUNT(DISTINCT CASE WHEN event = 'choosedelivery' THEN user_id END) AS choosedelivery_count,
    COUNT(DISTINCT CASE WHEN event = 'changepaymentmethod' THEN user_id END) AS changepayment_count,
    COUNT(DISTINCT CASE WHEN event = 'checkout' THEN user_id END) AS checkout_count,
    COUNT(DISTINCT CASE WHEN event = 'complete' THEN user_id END) AS complete_count
  FROM `etsy-funnel-analysis.etsyecommerce.events`
  WHERE EXTRACT(YEAR FROM timestamp) BETWEEN 2019 AND 2022
  GROUP BY year, quarter
)
SELECT
  year,
  quarter,
  100 AS product_view_cr,
  ROUND(IFNULL((addtocart_count * 100.0) / NULLIF(productview_count, 0), 0), 2) AS add_to_cart_cr,
  ROUND(IFNULL((viewcart_count * 100.0) / NULLIF(addtocart_count, 0), 0), 2) AS view_cart_cr,
  ROUND(IFNULL((chooseaddress_count * 100.0) / NULLIF(viewcart_count, 0), 0), 2) AS choose_address_cr,
  ROUND(IFNULL((choosedelivery_count * 100.0) / NULLIF(chooseaddress_count, 0), 0), 2) AS choose_delivery_cr,
  ROUND(IFNULL((changepayment_count * 100.0) / NULLIF(choosedelivery_count, 0), 0), 2) AS change_payment_cr,
  ROUND(IFNULL((checkout_count * 100.0) / NULLIF(changepayment_count, 0), 0), 2) AS checkout_cr,
  ROUND(IFNULL((complete_count * 100.0) / NULLIF(checkout_count, 0), 0), 2) AS complete_cr
FROM funnel_counts
ORDER BY year, quarter;
```

### 3. **What are the intermediate (bonus) conversion rates between key funnel stages? (Bonus Rates)** 

```sql
WITH funnel_counts AS (
  SELECT
    EXTRACT(YEAR FROM timestamp) AS year,
    EXTRACT(QUARTER FROM timestamp) AS quarter,

    COUNT(DISTINCT CASE WHEN event = 'productview' THEN user_id END) AS productview_count,
    COUNT(DISTINCT CASE WHEN event = 'addtocart' THEN user_id END) AS addtocart_count,
    COUNT(DISTINCT CASE WHEN event = 'viewcart' THEN user_id END) AS viewcart_count,
    COUNT(DISTINCT CASE WHEN event = 'chooseaddress' THEN user_id END) AS chooseaddress_count,
    COUNT(DISTINCT CASE WHEN event = 'choosedelivery' THEN user_id END) AS choosedelivery_count,
    COUNT(DISTINCT CASE WHEN event = 'changepaymentmethod' THEN user_id END) AS changepayment_count,
    COUNT(DISTINCT CASE WHEN event = 'checkout' THEN user_id END) AS checkout_count,
    COUNT(DISTINCT CASE WHEN event = 'complete' THEN user_id END) AS complete_count
  FROM `etsy-funnel-analysis.etsyecommerce.events`
  WHERE EXTRACT(YEAR FROM timestamp) BETWEEN 2019 AND 2022
  GROUP BY year, quarter
)
SELECT
  year,
  quarter,
  ROUND(IFNULL((checkout_count * 100.0) / NULLIF(addtocart_count, 0), 0), 2) AS addtocart_to_checkout_br,
  ROUND(IFNULL((checkout_count * 100.0) / NULLIF(viewcart_count, 0), 0), 2) AS viewcart_to_checkout_br,
  ROUND(IFNULL((checkout_count * 100.0) / NULLIF(chooseaddress_count, 0), 0), 2) AS chooseaddress_to_checkout_br,
  ROUND(IFNULL((checkout_count * 100.0) / NULLIF(choosedelivery_count, 0), 0), 2) AS choosedelivery_to_checkout_br,
  ROUND(IFNULL((checkout_count * 100.0) / NULLIF(changepayment_count, 0), 0), 2) AS changepayment_to_checkout_br,
  ROUND(IFNULL((complete_count * 100.0) / NULLIF(checkout_count, 0), 0), 2) AS checkout_to_complete_br
FROM funnel_counts
ORDER BY year, quarter;
```

### 4. ** What is the cart abandonment rate across quarters?**

```sql
--Cart Abandonment Rate (2019–2022)
WITH cart_data AS (
  SELECT
    EXTRACT(YEAR FROM timestamp) AS year,
    EXTRACT(QUARTER FROM timestamp) AS quarter,
    user_id,

    COUNT(CASE WHEN event = 'addtocart' THEN 1 END) AS add_to_cart_count,
    COUNT(CASE WHEN event = 'complete' THEN 1 END) AS complete_purchase_count
  FROM `etsy-funnel-analysis.etsyecommerce.events`
  WHERE EXTRACT(YEAR FROM timestamp) BETWEEN 2019 AND 2022
  GROUP BY year, quarter, user_id
)
SELECT
  year,
  quarter,
  ROUND(IFNULL(
    (COUNT(CASE WHEN add_to_cart_count > 0 AND complete_purchase_count = 0 THEN 1 END) * 100.0) 
    / NULLIF(COUNT(CASE WHEN add_to_cart_count > 0 THEN 1 END), 0), 0), 2) AS cart_abandonment_rate
FROM cart_data
GROUP BY year, quarter
ORDER BY year, quarter;
```
