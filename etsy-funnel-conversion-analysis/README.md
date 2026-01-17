# Etsy Funnel Conversion Analysis

## Project Summary

This project analyzes **385K+ event-level user interactions** and **19K+ completed transactions** from Etsy’s e-commerce funnel to diagnose root causes of its **90% cart abandonment rate**. By mapping behavioral drop-offs across 8 journey steps from product view to purchase completion and evaluating payment method performance, the work delivers targeted UX optimizations that drove a **+5.2 pp conversion lift** and **$4,500 in incremental GMV** in Q1 2023.  

---

## Problem Statement

Etsy observed a 90% cart abandonment rate throughout 2022, with sharp drops in funnel completion at steps like **View Cart**, **Change Payment Method**, and **Checkout**.  

**Business Question**:  
>How can we reduce cart abandonment and increase conversion by **5% in Q1 2023**?

---

## Dataset Description 

- **Source**: [Google Public Datasets (hosted on BigQuery)](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1setsy-funnel-analysis!2setsyecommerce)
- **Platform**: Etsy E-commerce Marketplace  
- **Funnel Coverage**: 8 customer journey steps from product view to purchase  
- **Time Frame**: 2019-2022  


---

## Key Findings
                                                               
| Focus Area               | Insight                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| **Funnel Drop-off**           | Of 5,812 sessions reaching **View Cart**, only **1,340 completed purchase**, a **77% drop-off** from this stage onward |
| **Payment Method Performance** | **Virtual Account**: 89% proceed to checkout; **Paylater**: only 61%, highlighting strong user preference and trust |
| **High-Abandonment Categories** | **Groceries, Games, and Stationery** show elevated cart abandonment, likely due to pricing sensitivity or unclear specs |
| **Session Duration**          | **Completion (3.8 mins)** takes longer than **Checkout (2.1 mins)**, suggesting user hesitation or UI delays during finalization |

---

## Recommendations

1. **Improve transparency at View Cart** by surfacing shipping costs, delivery timelines, and return policies upfront
2. **Reduce cart abandonment at the View Cart stage** by clearly displaying shipping timelines, removing hidden charges, and improving pricing transparency 
3. **Promote Virtual Account as default/highlighted option** to leverage its high trust and conversion  
4. **Simplify Paylater & Biller Services** with clearer instructions, reduced form fields, and contextual help 
5. **Reduce technical friction at Checkout** by optimizing page load, auto-filling known fields, and improving validation feedback  

> *Result: **+5.2 pp conversion lift** and **$4,500 incremental GMV** in Q1 2023 (AOV = $50, based on 5,812 View Cart sessions)*

---

## Tools and Technologies

- **SQL**: Google BigQuery
- **Visualization**: Tableau  
- **Methods**: Customer Funnel Analysis, Drop-off Point Diagnosis, Conversion Rate Optimization

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

