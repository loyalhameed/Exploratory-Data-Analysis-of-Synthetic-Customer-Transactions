import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

# Set a random seed for reproducibility
np.random.seed(42)

# Define the number of transactions
…    purchase_std,
    purchase_quartiles.to_string(),
    correlation
)

# Save descriptive statistics to a text file
stats_filepath = os.path.join(output_dir, 'descriptive_statistics.txt')
with open(stats_filepath, 'w') as f:
    f.write(descriptive_stats_text)
print(f"Saved descriptive statistics to {stats_filepath}")
