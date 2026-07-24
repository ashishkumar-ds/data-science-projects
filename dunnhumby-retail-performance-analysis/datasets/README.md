# Datasets

This folder is intentionally empty in git. The raw CSVs are excluded via
`.gitignore` because `transaction_data.csv` alone is ~140MB, over GitHub's
100MB hard limit on pushed files.

## Source

**dunnhumby "The Complete Journey"** — household-level transactions from
2,500 households over a 2-year period. Publicly available two ways:

- dunnhumby's own Source Files program: https://www.dunnhumby.com/source-files/

## Required files

Download and place these 7 files directly in this folder
(`notebooks/store_performance_analysis.ipynb` reads them via `../datasets/`):

| File | Approx. size | Contents |
|---|---|---|
| `transaction_data.csv` | 142 MB | Household-level purchase transactions |
| `product.csv` | 6.4 MB | Product catalog (department, brand, size) |
| `coupon.csv` | 2.8 MB | Coupon-to-eligible-product mapping |
| `coupon_redempt.csv` | 54 KB | Actual coupon redemptions by household |
| `campaign_desc.csv` | < 1 KB | Campaign start/end day windows |
| `campaign_table.csv` | 96 KB | Which households received which campaigns |
| `hh_demographic.csv` | 43 KB | Household demographics (partial coverage) |


## After downloading

```
datasets/
├── transaction_data.csv
├── product.csv
├── coupon.csv
├── coupon_redempt.csv
├── campaign_desc.csv
├── campaign_table.csv
└── hh_demographic.csv
```

Then run `notebooks/store_performance_analysis.ipynb` top to bottom. It
regenerates everything downstream, including the model artifacts consumed
by `api/app/`.
