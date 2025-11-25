import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

# Set a random seed for reproducibility
np.random.seed(42)

# Define the number of transactions
num_transactions = 500

# Create a list of TransactionIDs
transaction_ids = np.arange(1, num_transactions + 1)

# Generate a list of random CustomerAge values (18-70)
customer_age = np.random.randint(18, 71, num_transactions)

# Generate a list of random PurchaseAmount values ($10-$500)
purchase_amount = np.round(np.random.uniform(10, 500, num_transactions), 2)

# Generate a list of random TransactionDate values (within the last year)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

transaction_dates = [
    end_date - timedelta(days=np.random.randint(0, 366))
    for _ in range(num_transactions)
]

# Combine these lists into a pandas DataFrame
df_transactions = pd.DataFrame({
    'TransactionID': transaction_ids,
    'CustomerAge': customer_age,
    'PurchaseAmount': purchase_amount,
    'TransactionDate': transaction_dates
})

print("Synthetic dataset generated successfully:")
print(df_transactions.head())
print(f"\nDataFrame shape: {df_transactions.shape}")

print("\nFirst 5 rows of the dataset:")
print(df_transactions.head())

print("\nConcise summary of the dataset:")
df_transactions.info()

print("\nMissing values per column:")
print(df_transactions.isnull().sum())

# Create 'output' directory if it doesn't exist
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# Descriptive statistics for CustomerAge
age_stats = df_transactions['CustomerAge'].describe()
print("\nDescriptive statistics for CustomerAge:")
print(age_stats)

# Descriptive statistics for PurchaseAmount
purchase_mean = df_transactions['PurchaseAmount'].mean()
purchase_median = df_transactions['PurchaseAmount'].median()
purchase_std = df_transactions['PurchaseAmount'].std()
purchase_quartiles = df_transactions['PurchaseAmount'].quantile([0.25, 0.5, 0.75])

print("\nDescriptive statistics for PurchaseAmount:")
print(f"Mean: {purchase_mean:.2f}")
print(f"Median: {purchase_median:.2f}")
print(f"Standard Deviation: {purchase_std:.2f}")
print("Quartiles:")
print(purchase_quartiles)

# Generate and save histogram for PurchaseAmount
plt.figure(figsize=(10, 6))
plt.hist(df_transactions['PurchaseAmount'], bins=30, edgecolor='black')
plt.title('Distribution of Purchase Amount')
plt.xlabel('Purchase Amount ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig(os.path.join(output_dir, 'purchase_amount_histogram.png'))
plt.close() # Close the plot to prevent it from displaying inline unnecessarily
print(f"Saved histogram to {os.path.join(output_dir, 'purchase_amount_histogram.png')}")

# Generate and save scatter plot for CustomerAge vs. PurchaseAmount
plt.figure(figsize=(10, 6))
plt.scatter(df_transactions['CustomerAge'], df_transactions['PurchaseAmount'], alpha=0.6)
plt.title('Customer Age vs. Purchase Amount')
plt.xlabel('Customer Age')
plt.ylabel('Purchase Amount ($)')
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'age_vs_purchase_scatter.png'))
plt.close() # Close the plot to prevent it from displaying inline unnecessarily
print(f"Saved scatter plot to {os.path.join(output_dir, 'age_vs_purchase_scatter.png')}")

# Create a string containing descriptive statistics
descriptive_stats_text = """
Descriptive Statistics for Customer Transactions

CustomerAge:
{}

PurchaseAmount:
Mean: {:.2f}
Median: {:.2f}
Standard Deviation: {:.2f}
Quartiles:
{}
""".format(
    age_stats.to_string(),
    purchase_mean,
    purchase_median,
    purchase_std,
    purchase_quartiles.to_string()
)

# Save descriptive statistics to a text file
stats_filepath = os.path.join(output_dir, 'descriptive_statistics.txt')
with open(stats_filepath, 'w') as f:
    f.write(descriptive_stats_text)

print(f"Saved descriptive statistics to {stats_filepath}") 


correlation = df_transactions['CustomerAge'].corr(df_transactions['PurchaseAmount'])
print(f"Pearson's Correlation Coefficient between CustomerAge and PurchaseAmount: {correlation:.2f}")
