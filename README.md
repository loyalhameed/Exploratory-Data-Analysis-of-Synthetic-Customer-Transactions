# Full EDA Project
# Complete project structure.
# Exploratory Data Analysis of Synthetic Customer Transactions

This repository contains a complete assessment-ready EDA project for synthetic customer transactions.

## Contents
- `data/synthetic_transactions.csv` — generated dataset (1000 records).
- `eda.py` — self-contained script that performs inspection, statistics, and creates two plots.
- `notebook.ipynb` — simple notebook for interactive review.
- `report.md` — concise report and interpretation (<=250 words).
- `outputs/` — generated outputs after running `eda.py`.

## How to run
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python eda.py
