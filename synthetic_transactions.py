# -*- coding: utf-8 -*-
"""EDA of Synthetic Customer Transactions Data.ipynb

"""

#!/usr/bin/env python3
"""
synthetic_transactions.py
Self-contained EDA for synthetic customer transactions.

Produces:
- data/synthetic_transactions.csv (if not present)
- outputs/inspection.csv
- outputs/descriptive_stats.csv
- outputs/summary.txt
- outputs/figures/hist_purchase_amount.png
- outputs/figures/scatter_age_purchase.png

Usage:
    pip install -r requirements.txt
    python eda_of_synthetic_customer_transactions_data.py
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

BASE = os.getcwd()
DATA_DIR = os.path.join(BASE, "data")
OUT_DIR = os.path.join(BASE, "outputs")
FIG_DIR = os.path.join(OUT_DIR, "figures")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

CSV_PATH = os.path.join(DATA_DIR, "synthetic_transactions.csv")

def generate_dataset(n=500, seed=42):
    """Generate synthetic dataset and save to CSV."""
    np.random.seed(seed)
    transaction_ids = [f"T{100000+i}" for i in range(n)]
    ages = np.random.randint(18, 80, size=n)
    # Purchase amount: exponential-like with noise, then clamp
    purchase_amount = np.round(np.random.exponential(scale=80, size=n) + np.random.normal(0,10,size=n), 2)
    purchase_amount = np.clip(purchase_amount, 10, 1000)
    # random dates within last 365 days
    end = pd.to_datetime("today")
    start = end - pd.Timedelta(days=365)
    timestamps = np.random.randint(int(start.value//10**9), int(end.value//10**9), size=n)
    dates = pd.to_datetime(timestamps, unit='s')
    df = pd.DataFrame({
        "TransactionID": transaction_ids,
        "CustomerAge": ages,
        "PurchaseAmount": purchase_amount,
        "TransactionDate": dates
    })
    df = df.sample(frac=1, random_state=1).reset_index(drop=True)
    df.to_csv(CSV_PATH, index=False)
    return df

def load_dataset():
    if not os.path.exists(CSV_PATH):
        print("Dataset not found. Generating synthetic dataset (500 rows).")
        return generate_dataset(n=500)
    else:
        return pd.read_csv(CSV_PATH, parse_dates=["TransactionDate"])

def initial_inspection(df):
    dtypes = df.dtypes.to_frame("dtype")
    dtypes["nulls"] = df.isnull().sum().values
    dtypes["n_unique"] = df.nunique().values
    dtypes.to_csv(os.path.join(OUT_DIR, "inspection.csv"))
    return dtypes

def descriptive_statistics(df):
    desc = df[["CustomerAge","PurchaseAmount"]].describe().T
    desc["iqr"] = desc["75%"] - desc["25%"]
    desc.to_csv(os.path.join(OUT_DIR, "descriptive_stats.csv"))
    return desc

def textual_summary(df, max_chars=250):
    lines = []
    lines.append(f"Total transactions: {len(df)}")
    lines.append(f"Date range: {df.TransactionDate.min().date()} to {df.TransactionDate.max().date()}")
    lines.append("CustomerAge - mean, median, std: " + ", ".join([f"{x:.2f}" for x in [df.CustomerAge.mean(), df.CustomerAge.median(), df.CustomerAge.std()]]))
    lines.append("PurchaseAmount - mean, median, std: " + ", ".join([f"{x:.2f}" for x in [df.PurchaseAmount.mean(), df.PurchaseAmount.median(), df.PurchaseAmount.std()]]))
    summary = " | ".join(lines)
    with open(os.path.join(OUT_DIR, "summary.txt"), "w") as f:
        f.write(summary[:max_chars])
    return summary

def create_visualizations(df):
    # Histogram of PurchaseAmount
    plt.figure()
    plt.hist(df.PurchaseAmount, bins=40)
    plt.title("Distribution of PurchaseAmount")
    plt.xlabel("PurchaseAmount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    hist_path = os.path.join(FIG_DIR, "hist_purchase_amount.png")
    plt.savefig(hist_path)
    plt.close()

    # Scatter: CustomerAge vs PurchaseAmount
    plt.figure()
    plt.scatter(df.CustomerAge, df.PurchaseAmount, s=10)
    plt.title("CustomerAge vs PurchaseAmount")
    plt.xlabel("CustomerAge")
    plt.ylabel("PurchaseAmount")
    plt.tight_layout()
    scatter_path = os.path.join(FIG_DIR, "scatter_age_purchase.png")
    plt.savefig(scatter_path)
    plt.close()
    return hist_path, scatter_path

def main():
    df = load_dataset()
    print("Rows:", len(df))
    print("Date range:", df.TransactionDate.min().date(), "to", df.TransactionDate.max().date())

    inspection = initial_inspection(df)
    print("Inspection saved (outputs/inspection.csv)")

    desc = descriptive_statistics(df)
    print("Descriptive stats saved (outputs/descriptive_stats.csv)")

    summary = textual_summary(df)
    print("Text summary saved (outputs/summary.txt)")
    hist_path, scatter_path = create_visualizations(df)
    print("Figures saved:", hist_path, scatter_path)
    print("EDA complete. Check the outputs/ directory for deliverables.")

if __name__ == "__main__":
    main()

from IPython.display import Image
hist_path = "/content/outputs/figures/hist_purchase_amount.png"
display(Image(filename=hist_path))

from IPython.display import Image
scatter_path = "/content/outputs/figures/scatter_age_purchase.png"
display(Image(filename=scatter_path))
