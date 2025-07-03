# Etsy Funnel Analysis

## Project Summary

This project analyzes Etsy’s e-commerce funnel to uncover critical bottlenecks in the customer journey and reduce the company’s exceptionally high **90% cart abandonment rate**. By examining user behavior across each step of the funnel from browsing to purchase, the analysis identifies key drop-off points and provides data-driven recommendations to increase conversion rates by 5% in Q1 2023.  

---

## Problem Statement

Etsy observed a 90% cart abandonment rate throughout 2022, with sharp drops in funnel completion at steps like **View Cart**, **Change Payment Method**, and **Checkout**.  

**Business Question:**  
What are the main reasons behind Etsy’s high cart abandonment rate, and how can conversion be improved across the funnel?

---

## Funnel Analysis Scope

- **Source**: Google Public Datasets (hosted on BigQuery)
- **Platform**: Etsy E-commerce Marketplace  
- **Funnel Coverage**: 8 customer journey steps from product view to purchase  
- **Time Frame**: Q1 – Q4 2022  


---

## Key Findings

| Funnel Stage         | Insight                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------|
| View Cart            | Highest drop-off (−1,239 visitors); customers often abandon after reviewing their cart    |
| Checkout             | 27.01% bounce rate; possible delays or unclear details cause last-minute hesitation       |
| Completion           | Final conversion drops to 62.44%; session duration is longest, suggesting friction         |
| Payment Method       | Virtual Account had highest CR; Paylater & Biller Services had low CR and higher drop-off |
| Product Categories   | Categories like Games, Stationery & Sports had the highest CAR due to unclear specs or price |

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
etsy-funnel-analysis/
│
├── notebooks/           # SQL queries and funnel metrics analysis
│
├── presentation/        # Final project deck for business stakeholders
│   └── presentation_deck.pdf
│
├── README.md

