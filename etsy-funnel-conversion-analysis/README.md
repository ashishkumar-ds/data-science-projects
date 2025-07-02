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


1. **Reduce Cart Abandonment at View Cart Stage**  
   - Clearly show shipping times, fees, and remove hidden charges  
2. **Improve Other Payment Methods (Paylater, Biller Services)**  
   - Simplify UI/UX and provide clear FAQs to reduce uncertainty  
3.  **Capitalize on Virtual Account Popularity**  
   - Highlight this method visually and explain the process clearly to build trust
4. **Fix Checkout Friction**  
   - Streamline steps and reduce page load or validation issues that cause drop-offs  

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

