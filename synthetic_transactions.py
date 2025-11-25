import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

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

print("\nDescriptive statistics for CustomerAge:")
print(df_transactions['CustomerAge'].describe())

print("\nDescriptive statistics for PurchaseAmount:")
print(f"Mean: {df_transactions['PurchaseAmount'].mean():.2f}")
print(f"Median: {df_transactions['PurchaseAmount'].median():.2f}")
print(f"Standard Deviation: {df_transactions['PurchaseAmount'].std():.2f}")
print("Quartiles:")
print(df_transactions['PurchaseAmount'].quantile([0.25, 0.5, 0.75]))

plt.figure(figsize=(10, 6))
plt.hist(df_transactions['PurchaseAmount'], bins=30, edgecolor='black')
plt.title('Distribution of Purchase Amount')
plt.xlabel('Purchase Amount ($)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df_transactions['CustomerAge'], df_transactions['PurchaseAmount'], alpha=0.6)
plt.title('Customer Age vs. Purchase Amount')
plt.xlabel('Customer Age')
plt.ylabel('Purchase Amount ($)')
plt.grid(True)
plt.show()
