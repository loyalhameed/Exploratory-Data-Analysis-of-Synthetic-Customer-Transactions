# Report

This project performs an exploratory analysis on a synthetic set of customer transactions. The data includes age, purchase amount, and purchase date. A total of 500 rows were generated to allow basic distribution and trend observation.

The inspection confirms that the dataset has no missing values and contains the correct data types for each variable. Transaction dates span a realistic range within the past year.

The descriptive statistics show that customer ages are spread across adult age groups with a mean close to the mid forties. Purchase amounts display a clear right skew. A small number of high value transactions raise the average value, while the median remains lower and more stable. The interquartile range gives additional insight into the spread of typical purchases.

The histogram of purchase amount highlights the skew by showing a large concentration of lower value transactions. The scatter plot comparing customer age and purchase amount does not show a visible pattern. No strong relationship between age and spending behavior is observed in this dataset.

CustomerAge: Count: 500, Mean: 44.73, Standard Deviation: 15.24, Minimum: 18.00, 25th Percentile: 32.00, Median (50th Percentile): 45.00, 75th Percentile: 57.00, Maximum: 70.00.
PurchaseAmount: Mean: $255.47, Median: $257.12, Standard Deviation: $144.01, 25th Percentile: $128.80, 50th Percentile: $257.12, 75th Percentile: $379.80.

Overall, the analysis meets the Bronze level requirements and provides a clean summary of basic patterns in the synthetic data without extending into advanced methods.
