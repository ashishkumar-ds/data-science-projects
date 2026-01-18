# Gojek App Event Journey Mapping for Experimentation

## Project Summary

This project maps the end-to-end user journey within the Gojek app for a returning GoFood customer to define **standardized event names**, **measurable behavioral metrics**, and **key tracking fields**. The output enables Gojek’s product and data teams to run **structured in-app experiments**, detect **friction points**.

---

## Problem Statement

As a Data Analyst at Gojek, my task was to work with product and business teams to identify the **right metrics for experimentation**. To do this, I needed to:  
- Choose a specific customer journey  
- Act as a customer and document each step  
- Define **event names**, **metrics to track**, **data to collect**, and provide **example values**


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

| Step                        | Event Name               | Metric Example                                     |
|-----------------------------|---------------------------|----------------------------------------------------|
| OTP Verification            | `otp_verification`        | **OTP Success Rate**, Avg Verification Time         |
| GoFood Icon Click           | `gofood_selected`         | **Selection Rate**, **Abandonment Rate**            |
| Restaurant Filter Use       | `find_restaurant`         | **Cuisine/Price Filter Usage**, **Conversion Rate** |
| Add Item to Cart            | `item_added_to_cart`      | **Cart Size**, **Abandonment Rate**                 |
| Promo Code Applied          | `apply_coupon`            | **Promo Usage Rate**, Avg Discount                  |
| Payment Method Selection    | `select_payment_method`   | **GoPay % Usage**, **Inactive Payment Method Rate** |
| Place Order                 | `order_placed`            | **Order Completion Rate**, **Avg Order Value**      |
| Delivery Completion         | `order_delivered`         | **Avg Delivery Time**, **Delivery Success Rate**    |
| Feedback Provided           | `driver_app_rating`       | **Avg Rating**, **Feedback Sentiment**              |

---

## Tools & Techniques

- **Lucidchart**
- **Customer Journey Mapping**    
- **Funnel-Based Metric Definition**

---

## Project Structure

```bash
gojek-app-event-mapping/
│
├── presentation/       # Final project walkthrough deck
│   └── presentation_deck.pdf
│
└── README.md
