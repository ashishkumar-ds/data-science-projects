# TheLook E-commerce Growth & Retention Analysis

## Project Summary

This project analyzes synthetic e-commerce clothing data from TheLook to uncover key insights into product profitability, customer purchasing behavior, and retention trends. After facing significant operational challenges in 2023, the company turned to data to guide its optimization efforts. Using SQL (BigQuery) for cohort analysis and Looker Studio for interactive reporting, this project provides decision-makers with evidence-based recommendations to improve category performance, retention, and profitability.

---

## Problem Statement

What strategies can TheLook adopt post-2023 to boost retention and category performance through insights from customer and order data?

---

## Dataset Description

- **Source**: Synthetic dataset created by Looker  
- **Total Records**: 65,000+ orders  
- **Time Frame**: Multi-year retail activity until end of 2023  
- **Key Tables & What They Contain**:
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

1. **Investigate cancel/return reasons** to fix funnel or product issues  
2. **Follow up with high-return users** for feedback and friction points  
3. **Promote fast-growing categories** (Swim, Active, Leggings) with targeted campaigns  
4. **Remove low-margin products** that aren't scaling with volume  
5. **Boost retention post-6 months** with personalized offers, A/B testing, and cohort tracking  
6. **Increase inventory** for proven high-profit categories (e.g., Outerwear & Coats)  

---

## Tools & Technologies

- **SQL** 
- **Looker Studio** 
- **Cohort Analysis**
  
---

## Project Structure

```bash
thelook-ecommerce-retention-analysis/
│
├── notebooks/             # SQL queries and modeling logic (if added)
│
├── dashboard/             # Looker Studio screenshot or dashboard links
│
├── presentation/          # Final stakeholder-ready pitch deck
│   └── thelook_pitch_deck.pdf
│
└── README.md

