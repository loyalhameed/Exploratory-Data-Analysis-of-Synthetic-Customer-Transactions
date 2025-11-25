# Exploratory Data Analysis of Synthetic Customer Transaction Analysis

## Project Overview

This project involves generating and analyzing a synthetic dataset of customer transactions. It covers key data science steps including data generation, inspection, descriptive statistics, and basic visualization, culminating in a concise written analysis of the findings.
This project completes the EDA tasks. The goal is to generate a synthetic dataset, run initial inspection, compute descriptive statistics, and create two required plots.


## Project Tasks
1. Generate a synthetic dataset of customer transactions.
2. Perform initial inspection of data types, missing values, and unique counts.
3. Produce descriptive statistics for numerical fields.
4. Create two plots:
   - Histogram of PurchaseAmount
   - Scatter plot of CustomerAge vs PurchaseAmount

## Dataset Generation

A synthetic dataset of 500 customer transactions was generated with the following columns:
- `TransactionID`: Unique identifier for each transaction.
- `CustomerAge`: Age of the customer (ranging from 18 to 70).
- `PurchaseAmount`: Amount of the purchase (ranging from $10 to $500).
- `TransactionDate`: Date of the transaction (within the last year).

## Data Inspection

Initial data inspection was performed using Pandas to verify data types, check for missing values, and display sample rows. The dataset was found to be complete and correctly formatted.

## Descriptive Statistics

Descriptive statistics were computed for:
- `CustomerAge`: Summary statistics (count, mean, std, min, 25%, 50%, 75%, max).
- `PurchaseAmount`: Mean, median, standard deviation, and quartiles.

## Visualizations

Two key visualizations were created:
1.  **Histogram of PurchaseAmount**: To illustrate the distribution of customer spending.
2.  **Scatter Plot of CustomerAge vs. PurchaseAmount**: To explore potential relationships or trends between customer age and their purchase amounts.

## Analysis of Findings

This section will summarize the key observations from the descriptive statistics and visualizations, focusing on:
- The distribution of customer ages.
- The central tendency and variability of purchase amounts.
- Any discernible trends or lack thereof between customer age and purchase behavior.

## Setup and Usage

This project is implemented in a Python Jupyter/Colab notebook. To run the analysis, simply execute the cells in sequence.


## How to Run
pip install -r requirements.txt
python src/synthetic_customer_transactions.py

## Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib


# Summary:
Q&A

What are the computed numeric descriptive statistics for 'CustomerAge' and 'PurchaseAmount'?

CustomerAge: Count: 500, Mean: 44.73, Standard Deviation: 15.24, Minimum: 18.00, 25th Percentile: 32.00, Median (50th Percentile): 45.00, 75th Percentile: 57.00, Maximum: 70.00.
PurchaseAmount: Mean: $255.47, Median: $257.12, Standard Deviation: $144.01, 25th Percentile: $128.80, 50th Percentile: $257.12, 75th Percentile: $379.80.

