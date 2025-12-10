# Dunnhumby Retail Store Performance – Notebooks

This folder contains two Jupyter notebooks that document the complete analytical workflow for improving sales across underperforming stores using customer-level transaction data. The analysis focuses on segmentation, campaign evaluation, and revenue forecasting.

---

Tier 1 – Data Cleaning Notebook  
File: notebooks/data_cleaning.ipynb  

Objective  
Transform raw, multi-source retail transaction data into a unified, analysis-ready dataset with validated business logic and an optimized structure for downstream analytics.

2 Data Understanding

Feed	Rows	
Transaction	2 595 914	
Product	23 539	
Coupon	4 campaigns	
TOTAL	2 619 457	

3 Data Preparation

QC Gate	Rows Removed	% Raw	
Zero quantity	7 266	0.28	
Illegal positive discount	6 206	0.24	
Extreme outliers	10	0.00	
TOTAL REMOVED	13 472	0.52 %	

4 Feature Engineering

Feature	Definition	Business Role	
DATE	Julian → calendar date	time-series index	
DAY_CATEGORY	weekday / weekend	roster optimisation	
TIME_CATEGORY	Day (06-18) / Night (18-06)	store-hour decisions	
TIMES_CATEGORY	morning / afternoon / evening / night	promo timing	
cust_purchase_value	net spend (sales + coupon)	LTV modelling	
sales_lag_7	sales 7 days ago	auto-regressive signal	
sales_ma_7	7-day moving average	trend smoothing	

Artifact produced: clean_2_58M_rows_562stores.parquet

[→ Jump to Tier 2 Analysis](tier-2-analysis.md)

---

Tier 2 – Main Analysis Notebook  
File: notebooks/main_analysis.ipynb  

Objective  
Identify drivers of store performance, segment customers by value, and analyse campaign effectiveness to generate actionable recommendations for improving underperforming stores.

5 Exploratory Data Analysis

5.1 Store Concentration (Pareto)

Lens	Metric	Business Take-away	
Store universe	562 total stores	178 active after QC filters	
Store performance	top 19 % stores = 80 % sales	80/20 confirmed → capex focus list	

5.2 Customer Traffic Patterns

Time Dimension	Level	Footfall Share	Peak Indicator	
Week-part	weekday	65 %	▲ staff Mon-Fri	
	weekend	35 %	different promo cadence	
Time-of-day	afternoon (10-15 h)	31.8 %	▲ true peak, not evening	
	evening (16-21 h)	28.6 %	secondary peak	
	morning (04-09 h)	22.3 %	tertiary	
	night (22-03 h)	17.3 %	▼ maintenance window	

Insight: Afternoon weekday drives highest traffic → roster & promo budget skew 32 % to 10 AM–3 PM slot.

6 Campaign Uplift (Controlled Pre/Post)

Campaign	Cust. CR	Coupon CR	ROI	Sales Share	Incremental	Uplift vs Baseline	
15	0.8 %	4.8 %	25 %	13 %	1.1 M	+2.1 %	
16	4.4 %	8.7 %	194 %	17 %	2.0 M	+5.8 %	
17	1.8 %	5.0 %	114 %	22 %	2.6 M	+4.2 %	
18	13.0 %	9.1 %	235 %	47 %	5.5 M	+18.7 %	

Statistical Validation  
- Baseline: day 531-586 (n = 38 661)  
- Campaign: day 587-642 (n = 38 660)  
- Best-customer daily growth: +1.22 % → +2.60 % (Δ +113 %, p < 0.05, two-sided t-test)  
- 95 % CI for uplift: [+16.4 %, +21.0 %] → 5.0 M – 6.1 M incremental sales

7 Customer Segmentation (RFM) – Best-Customer Focus

Segment	% Cust	% Rev	Avg Monetary	Campaign-18 Redemp.	
Best	11 %	41 %	1 246	38 %	
Loyal	25 %	29 %	682	32 %	
Promising	31 %	19 %	413	18 %	
At-Risk	25 %	10 %	199	12 %	
Lost	8 %	2 %	75	0 %	

Insight: 11 % of customers deliver 41 % of revenue and account for 38 % of high-ROI campaign redemptions → prioritise retention & upspend on this tier.

8 Sales Forecast

Model	wMAPE	RMSE	MAE	R²	Train/Val/Test	95 % PI Width	
Linear Regression	5.4 %	842	512	0.78	70/15/15 %	± 1 649	
LightGBM + Optuna	3.1 %	488	296	0.92	same split	± 956	

Technical Details  
- Optuna tuned 50 hyper-parameter sets (early-stop 50 rounds).  
- Rolling-window 5-fold CV: mean wMAPE = 3.2 % ± 0.3 %.  
- Durbin-Watson = 1.98 (no auto-correlation); residual Shapiro p = 0.12 (Gaussian).  
- Production forecast: 60-day horizon, nightly refresh ≤ 15 s, CI width ± 956 (vs ± 1 649 baseline).

9 Business Impact
- Scale Campaign-18 mechanics → +12 M annualised (CI 10 M–14 M)  
- Deploy 3.1 % MAPE forecast → 342 k working-capital release (safety-stock reduction)  
- Re-fit / exit bottom-quintile stores (<1 % sales) → OpEx savings TBD

Stack: Python 3.9, pandas, LightGBM, Optuna – repo ready for staging pipeline.
