

# TheLook E-commerce Growth & Retention Analysis

## Project Summary

This project analyzes **65,166 customer orders** from TheLook’s e-commerce platform to diagnose operational inefficiencies in order fulfillment and product returns. By evaluating order status trends, return drivers, and user retention patterns across 2019–2022, the work identifies root causes of **15% cancellation and 10% return rates**, and delivers targeted interventions to improve customer trust, reduce friction, and increase long-term engagement.

---

## Problem Statement

The Look E-Commerce is in optimization mode due to a potential 2023 business crisis. Management plans to cut resources in categories with the lowest growth over the past year and needs data-driven strategies to improve user retention and reduce operational friction in order fulfillment.

**Business Question**:  
> How can we increase 6-month user retention and reduce cancellations and returns by analyzing customer behavior and order trends?

---

## Dataset Description

- **Source**: [Synthetic dataset created by Looker](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sthelook_ecommerce) 
- **Total Records**: 65,000+ orders
- **Platform**: TheLook (fashion & apparel e-commerce)    
- **Time Frame**: 2019-2022  

---

## Key Findings

| Focus Area            | Insight                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------|
| **Order Issues**           | 15% of orders were cancelled, and 10% were returned                                       |
| **High Return Users**      | **2,299 users returned 2,332 orders** – a small segment with high return activity           |
| **Profitability Gaps**     | Products like **Aluminum Aluma Wallet** sold poorly with very low margins                  |
| **Category Growth**        | **Swimwear, Activewear, and Leggings** showed the fastest growth                           |
| **Profit Leaders**         | **Outerwear and Coats** consistently drove the highest profits across months               |
| **Customer Patterns**      | **Average orders/user = 1 per month**, **average order value = $84.69**                    |
| **Retention Challenge**    | Cohorts grew month-over-month, but **dropped sharply in retention after 4–6 months**        |

---

## Recommendations

1. **Investigate cancel/return reasons** to fix funnel or product issues  
2. **Follow up with high-return users** for feedback and friction points  
3. **Promote fast-growing categories** (Swim, Active, Leggings) with targeted campaigns  
4. **Increase inventory for proven high-profit categories** (e.g., Outerwear & Coats)  
5. **Remove low-margin products** that aren't scaling with volume  
6. **Boost retention post-6 months** with personalized offers, A/B testing, and cohort tracking  

> *Expected Outcome: Reduce returns by 15–20%, lower cancellations by 10%, and improve 6-month retention by 8–12% through targeted UX and operational fixes.*

---

## Tools & Technologies

- **SQL**: Google BigQuery  
- **Visualization**: Looker Studio 
- **Methods**: Cohort Analysis, 

---

## Project Structure

```bash
thelook-ecommerce-retention-analysis/
│
├── notebooks/           # SQL queries for cohort analysis, product trends, and user behavior
│
├── dashboard/           # Looker Studio dashboard screenshot
│   └── dashboard_screenshot.jpg        
│
├── presentation/        # Final business presentation for non-technical stakeholders
│   └── presentation_deck.pdf
│
└── README.md

