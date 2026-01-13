# Etsy Funnel Conversion Analysis

## Project Summary

This project analyzes Etsy’s e-commerce funnel to uncover critical bottlenecks in the customer journey and reduce the company’s exceptionally high **90% cart abandonment rate**. By examining user behavior across each step of the funnel from browsing to purchase, the analysis identifies key drop-off points and provides data-driven recommendations to increase conversion rates by 5% in Q1 2023.  

---

## Problem Statement

Etsy observed a 90% cart abandonment rate throughout 2022, with sharp drops in funnel completion at steps like **View Cart**, **Change Payment Method**, and **Checkout**.  

**Business Question:**  
What are the main reasons behind Etsy’s high cart abandonment rate, and how can conversion be improved across the funnel?

---

## Dataset Description 

- **Source**: [Google Public Datasets (hosted on BigQuery)](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1setsy-funnel-analysis!2setsyecommerce)
- **Platform**: Etsy E-commerce Marketplace  
- **Funnel Coverage**: 8 customer journey steps from product view to purchase  
- **Time Frame**: 2019-2022  


---

## Key Findings

| Funnel Stage              | Insight                                                                                          |
|---------------------------|--------------------------------------------------------------------------------------------------|
| Homepage Visit            | Drop-off begins here, with many visitors bouncing without exploring products further             |
| View Product              | Some users exit after viewing a product, likely due to unclear information or pricing confusion  |
| Add to Cart               | Engagement remains strong, but early hesitation appears in lower-trust product categories         |
| View Cart                 | Major drop-off observed; users abandon after reviewing cart due to unexpected costs or shipping   |
| Change Payment Method     | Users switching from default methods often exit; confusion around Paylater and Biller Services   |
| Payment Method Selected   | Virtual Account performs well, while other options show lower confidence and higher abandonment  |
| Checkout                  | 27% bounce rate; users hesitate during form submission or encounter delays                        |
| Completion                | Final conversion rate drops to 62.44%; long session times suggest friction or lack of urgency     |


---

## Recommendations

1. **Reduce cart abandonment at the View Cart stage** by clearly displaying shipping timelines, removing hidden charges, and improving pricing transparency.

2. **Improve performance of Paylater and Biller Services** by simplifying the checkout experience and providing clear guidance or FAQs to reduce uncertainty.

3. **Capitalize on the popularity of the Virtual Account payment method** by visually highlighting it and clearly explaining the process to increase trust and usage.

4. **Fix friction in the checkout stage** by streamlining the steps, minimizing delays, and resolving any validation or technical blockers causing user hesitation.

---

## Tools and Techniques

- SQL (Google BigQuery)  
- Tableau (Dashboard Visualizations) 
- Customer Funnel Analysis  

---

## Project Structure

```bash
etsy-funnel-conversion-analysis/
│
├── notebooks/           # SQL queries and funnel metrics analysis
│
├── presentation/        # Final project deck for business stakeholders
│   └── presentation_deck.pdf
│
├── README.md

