# Gojek App Event Journey Mapping for Experimentation

## Project Summary

This project focuses on mapping the customer journey within the Gojek app to define meaningful product events and metrics for experimentation. Acting as a user ordering food through the GoFood service, the project breaks down the app journey into event-based milestones, from login to delivery. As a data analyst, I proposed standardized event names, experimentation-ready metrics, and key tracking fields to support product teams in defining actionable KPIs. These insights enable Gojek’s product and business teams to improve user experience, detect friction, and run structured in-app experiments.

---

## Problem Statement

**How can Gojek define and track meaningful product events across the user journey to support experimentation and enhance in-app experience?**


---

## Dataset Description

- **Source**: Real-time customer journey walkthrough (no backend data; all events, metrics, and tracking schema were defined manually)
- **Journey Focus**: Returning customer placing a GoFood order  
- **Platform**: Gojek app (Indonesia-based multi-service platform)  
- **Use Case**: Food ordering through GoFood, 2x per week customer pattern  
- **Data Captured**: Event name, timestamp, user ID, screen activity, selected actions, and user feedback

---

## Customer Journey Covered

The journey spans 15+ app interactions and milestones:

1. App Install & Launch  
2. Login / Sign Up  
3. Input Mobile Number  
4. OTP Verification  
5. Landing on Home Page  
6. Click GoFood Icon  
7. Use “Near Me” Filter  
8. Select Restaurant  
9. Choose Food / Drink  
10. Apply Coupon / Promo  
11. Select Payment Method  
12. Place Order  
13. Order Status & Driver Assigned  
14. Order Delivered  
15. Rate Driver / App  

---

## Key Deliverables

| Step                        | Event Name               | Metric Example                                     | Insights Tracked                                 |
|-----------------------------|---------------------------|----------------------------------------------------|--------------------------------------------------|
| OTP Verification            | `otp_verification`        | OTP Success Rate, Avg Verification Time            | Mobile auth efficiency by region/device          |
| GoFood Icon Click           | `gofood_selected`         | Selection Rate, Abandonment Rate                   | Interest in GoFood service                       |
| Restaurant Filter Use       | `find_restaurant`         | Cuisine/Price Filter Usage, Conversion Rate        | Filter impact on decision-making                 |
| Add Item to Cart            | `item_added_to_cart`      | Cart Size, Abandonment Rate                        | Popular dishes and cart drop-off                 |
| Promo Code Applied          | `apply_coupon`            | Promo Usage Rate, Avg Discount                     | Campaign effectiveness                           |
| Payment Method Selection    | `select_payment_method`   | Gopay % Usage, Inactive Payment Method Rate        | Preferred and unused payment options             |
| Place Order                 | `order_placed`            | Order Completion Rate, Avg Order Value             | Funnel completion indicators                     |
| Delivery Completion         | `order_delivered`         | Avg Delivery Time, Delivery Success Rate           | Operational efficiency, timing                   |
| Feedback Provided           | `driver_app_rating`       | Avg Rating, Feedback Sentiment                     | Satisfaction metrics for driver & app experience |

---

## Recommendations

1. Define standard event naming across product teams to ensure experiment tracking consistency  
2. Track real-time behavioral metrics like abandonment rates and promo usage to optimize UI/UX decisions  
3. Prioritize high-dropoff points (e.g., cart, payment) for experimentation or A/B testing  
4. Use feedback sentiment (text/NLP) to enrich app review signals and improve service quality  
5. Build dashboards to visualize these metrics over time and identify changes post feature releases

---

## Tools & Techniques

- Excel
- Product Journey Mapping     
- Sample Metric Table for Product Managers  

---

## Project Structure

```bash
gojek-app-event-mapping/
│
├── presentation/       # Final project walkthrough deck
│   └── presentation.pdf
│
└── README.md
