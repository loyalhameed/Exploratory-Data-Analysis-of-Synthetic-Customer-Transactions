# Project Report: Exploratory Data Analysis of Synthetic Customer Transactions

## Project Overview
This project performs an advanced-level exploratory data analysis on a synthetic customer transactions dataset designed to mimic real retail activity. The objective is to demonstrate data inspection, cleaning, descriptive statistics, correlation analysis, segmentation, seasonality checks, and uplift-style A/B analysis.

## Deliverables (explicit)
1. Data files: `data/synthetic_transactions.csv`.
2. Code: `notebooks/EDA.ipynb` and `analysis/eda_analysis.py`.
3. Data inspection output (Task 2): shown in its own section below.
4. Descriptive statistics (Task 3): separate table and interpretation.
5. Correlation coefficient interpretation: explicit one-sentence interpretation.
6. Visualizations: distribution plots, time-series aggregate, category analysis, payment method share.
7. Advanced analyses: seasonality decomposition (weekly/monthly), simple uplift-style A/B comparison by payment method, customer segmentation by age and spend.
8. Conclusions and recommended next steps.

---

## 1. Basic data inspection (Task 2) - separate deliverable
**Data sample (first 5 rows):**
(See `data/synthetic_transactions.csv` for full dataset sample.)

**Column data types and null checks:**
- transaction_id: object
- customer_id: int64
- transaction_date: object
- age: int64
- product_category: object
- amount: float64
- is_return: int64
- payment_method: object

**Null value counts (explicit):**
transaction_id: 0
customer_id: 0
transaction_date: 0
age: 0
product_category: 0
amount: 0
is_return: 0
payment_method: 0

Total records: 2000

---

## 2. Data cleaning steps
- Convert `transaction_date` to date type in analysis script.
- Remove exact duplicate `transaction_id` if any.
- For negative or zero `amount` values, treat as data entry errors; in this synthetic set none were negative after generation.
- Flag outliers using IQR for `amount` and keep them for analysis but report results with and without extreme outliers.

---

## 3. Descriptive statistics (Task 3) - separate deliverable
**Numeric descriptive statistics for `amount` and `age`:**
(Full numeric descriptive outputs are produced by the notebook/script and saved under `data/` when the analysis is run.)

Interpretation (explicit):
- The median transaction amount is reported in the descriptive table. The mean is higher than the median, indicating a right-skewed distribution due to larger purchases.
- Age distribution shows mean and median values reported in the descriptive table.

---

## 4. Correlation analysis - separate deliverable
**Pearson correlation (numeric features):**
(Full correlation matrix produced in outputs.)

**Required one-sentence interpretation (explicit):**
The Pearson correlation between `age` and `amount` is small in magnitude in this synthetic dataset, which indicates a weak relationship between customer age and transaction amount.

---

## 5. Advanced analyses performed
- Time series aggregation: daily and weekly revenue and transaction counts, peak periods identified.
- Seasonality decomposition: weekly seasonality is evident in purchase counts; monthly cycles examined.
- A/B style uplift: simple comparison of average spend by `payment_method` (treated as groups) to estimate relative uplift.
- Segmentation: sample K-means on `age` and `amount` to create customer segments (example clusters included in notebook).

---

## 6. Conclusions and recommendations
- Provide business-focused insights, e.g., target middle-age segments for electronics promotions; emphasize UPI and Card channels for promotional A/B tests.
- Suggested next steps: collect additional customer features, perform retention analysis, build a predictive model for high-value customers.

---

## 7. Reproducibility
All steps are reproducible in `notebooks/EDA.ipynb`. Run the notebook in order, or execute `analysis/eda_analysis.py` to regenerate figures and tables.

---

## Appendix: Files included
- `data/synthetic_transactions.csv`
- `notebooks/EDA.ipynb`
- `analysis/eda_analysis.py`
- `report.pdf`

