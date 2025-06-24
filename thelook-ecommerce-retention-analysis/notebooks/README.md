**Business Questions:**  

1. How many unique users, orders, and total sales occurred per order status each month?

```sql
-- Calculate metrics for each month and status
SELECT
  DATE_TRUNC(CAST(created_at AS DATE), MONTH) AS month_year,  -- Extract month-year
  status,                                                     -- Order status (e.g., Complete, Cancelled, Returned)
  COUNT(DISTINCT user_id) AS total_unique_users,              -- Number of unique users
  COUNT(DISTINCT order_id) AS total_orders,                   -- Number of orders
  SUM(sale_price) AS total_sale_price                         -- Total sale price
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS oi
WHERE DATE_TRUNC(created_at, MONTH) BETWEEN '2019-01-01' AND '2022-08-01'
GROUP BY 1, 2
ORDER BY 1, 2;

 
2. Who are the users that returned orders in August 2022?

```sql
-- Retrieve user information for users who made a return in August 2022
SELECT
  u.id AS id,                  -- User ID
  u.email AS email,            -- User's email address
  u.first_name AS first_name,  -- User's first name
  u.last_name AS last_name     -- User's last name
FROM `bigquery-public-data.thelook_ecommerce.users` u
INNER JOIN `bigquery-public-data.thelook_ecommerce.orders` o
  ON u.id = o.user_id
WHERE DATE_TRUNC(o.created_at, MONTH) BETWEEN '2022-08-01' AND '2022-08-31'
  AND o.status = 'Returned';
