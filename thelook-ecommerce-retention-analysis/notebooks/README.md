# Notebooks: SQL Queries & Business Questions

This file documents all key SQL queries used in the project, each tied to a specific business question. It helps demonstrate how real-world questions were translated into data-driven answers using SQL and cohort analysis.

---

## Query 1: Monthly Summary of Users, Orders, and Sales by Status

**Business Question:**  
How many unique users, orders, and total sales occurred per order status each month?

```sql
SELECT
  DATE_TRUNC(CAST(created_at AS DATE), MONTH) AS month_year,
  status,
  COUNT(DISTINCT user_id) AS total_unique_users,
  COUNT(DISTINCT order_id) AS total_orders,
  SUM(sale_price) AS total_sale_price
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS oi
WHERE DATE_TRUNC(created_at, MONTH) BETWEEN '2019-01-01' AND '2022-08-01'
GROUP BY 1, 2
ORDER BY 1, 2;


## Query 2: Identify Users with Returned Orders

Business Question:
Who are the users that returned orders in August 2022?

SELECT
  u.id AS id,
  u.email AS email,
  u.first_name AS first_name,
  u.last_name AS last_name
FROM `bigquery-public-data.thelook_ecommerce.users` u
INNER JOIN `bigquery-public-data.thelook_ecommerce.orders` o
  ON u.id = o.user_id
WHERE DATE_TRUNC(o.created_at, MONTH) BETWEEN '2022-08-01' AND '2022-08-31'
  AND o.status = 'Returned';

