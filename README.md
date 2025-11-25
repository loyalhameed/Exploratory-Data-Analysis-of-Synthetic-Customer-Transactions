# Exploratory Data Analysis of Synthetic Customer Transactions

This project completes the EDA tasks. The goal is to generate a synthetic dataset, run initial inspection, compute descriptive statistics, and create two required plots.

## Project Tasks
1. Generate a synthetic dataset of customer transactions.
2. Perform initial inspection of data types, missing values, and unique counts.
3. Produce descriptive statistics for numerical fields.
4. Create two plots:
   - Histogram of PurchaseAmount
   - Scatter plot of CustomerAge vs PurchaseAmount
5. Write a short summary of findings under 250 characters.

# Summary:
Q&A

What are the computed numeric descriptive statistics for 'CustomerAge' and 'PurchaseAmount'?
CustomerAge: Count: 500, Mean: 44.73, Standard Deviation: 15.24, Minimum: 18.00, 25th Percentile: 32.00, Median (50th Percentile): 45.00, 75th Percentile: 57.00, Maximum: 70.00.
PurchaseAmount: Mean: $255.47, Median: $257.12, Standard Deviation: $144.01, 25th Percentile: $128.80, 50th Percentile: $257.12, 75th Percentile: $379.80.

## How to Run
pip install -r requirements.txt
python src/synthetic_customer_transactions.py
