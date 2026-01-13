# TheLook E-commerce Growth & Retention Analysis

## Project Summary

This project explores how TheLook, an e-commerce clothing brand, used data to recover from the impact of COVID-19 and a challenging 2023. By analyzing customer behavior, order patterns, and retention trends, it uncovers key insights and strategic opportunities to improve product performance, reduce churn, and drive sustainable growth.

---

## Problem Statement

What strategies can TheLook adopt post-2023 to boost retention and category performance through insights from customer and order data?

---

## Dataset Description

- **Source**: [Synthetic dataset created by Looker](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sthelook_ecommerce) 
- **Total Records**: 65,000+ orders  
- **Time Frame**: Multi-year retail activity until end of 2023  
- **Component Tables and Key Attributes**
  - `users` – Customer profiles and contact information  
  - `orders` – Purchase and return activity with timestamps  
  - `order_items` – Products in each order, pricing, and fulfillment status  
  - `products` – Product details (category, price, profitability)  
  - `inventory_items` – Inventory status and availability  
  - `events` – Customer behavioral events (e.g., page views, carts)  
  - `distribution_centers` – Fulfillment and delivery geography  

---

## Key Findings

| Focus Area            | Insight                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------|
| Order Issues           | 15% of orders were cancelled, and 10% were returned                                       |
| High Return Users      | 2,299 users returned 2,332 orders – a small segment with high return activity             |
| Profitability Gaps     | Products like Aluminum Aluma Wallet sold poorly with very low margins                    |
| Category Growth        | Swimwear, Activewear, and Leggings showed the fastest growth                             |
| Profit Leaders         | Outerwear and Coats consistently drove the highest profits across months                 |
| Customer Patterns      | Average orders/user = 1 per month, average order value = $84.69                          |
| Retention Challenge    | Cohorts grew month-over-month, but dropped sharply in retention after 4–6 months         |

---

## Recommendations

1. Investigate cancel/return reasons to fix funnel or product issues  
2. Follow up with high-return users for feedback and friction points  
3. Promote fast-growing categories (Swim, Active, Leggings) with targeted campaigns
4. Increase inventory for proven high-profit categories (e.g., Outerwear & Coats)  
5. Remove low-margin products that aren't scaling with volume  
6. Boost retention post-6 months with personalized offers, A/B testing, and cohort tracking 

---

## Tools & Technologies

- SQL (Google BigQuery) 
- Looker Studio 
- Cohort Analysis
  
---

## Project Structure

```bash
thelook-ecommerce-retention-analysis/
│
├── notebooks/           # SQL queries for cohort analysis, product trends, and user behavior
│
├── dashboard/           # Looker Studio dashboard link and (optional) screenshot
│   └── dashboard_screenshot.jpg        
│
├── presentation/        # Final business presentation for non-technical stakeholders
│   └── presentation_deck.pdf
│
└── README.md

