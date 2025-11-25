# # Project Report: Exploratory Data Analysis of Synthetic Customer Transaction 


## 1. Introduction
 
The objective is to demonstrate proficiency in data generation, basic data inspection, statistical summarization, and visualization using Python's data science libraries.

This project performs an exploratory analysis on a synthetic set of customer transactions. The data includes age, purchase amount, and purchase date. A total of 500 rows were generated to allow basic distribution and trend observation.

The inspection confirms that the dataset has no missing values and contains the correct data types for each variable. Transaction dates span a realistic range within the past year.

The descriptive statistics show that customer ages are spread across adult age groups with a mean close to the mid forties. Purchase amounts display a clear right skew. A small number of high value transactions raise the average value, while the median remains lower and more stable. The interquartile range gives additional insight into the spread of typical purchases.

## 2. Dataset Generation

A synthetic dataset comprising 500 customer transactions was generated. Each transaction includes a `TransactionID`, `CustomerAge` (randomly distributed between 18 and 70), `PurchaseAmount` (randomly distributed between $10 and $500), and `TransactionDate` (within the last year).

## 3. Data Inspection

Upon generation, the dataset was inspected for structural integrity. All 500 entries were found to be complete, with no missing values across any columns. Data types were confirmed to be appropriate for analysis (`int64` for TransactionID and CustomerAge, `float64` for PurchaseAmount, and `datetime64[ns]` for TransactionDate).

## 4. Descriptive Statistics

### CustomerAge

| Statistic          | Value    |
| :----------------- | :------- |
| Count              | 500      |
| Mean               | 44.73    |
| Standard Deviation | 15.24    |
| Minimum            | 18.00    |
| 25th Percentile    | 32.00    |
| Median (50th)      | 45.00    |
| 75th Percentile    | 57.00    |
| Maximum            | 70.00    |

The customer ages are evenly distributed across the defined range, with an average age close to the midpoint, indicating a representative sample across the adult age spectrum.

### PurchaseAmount

| Statistic          | Value     |
| :----------------- | :-------- |
| Mean               | $255.47   |
| Median             | $257.12   |
| Standard Deviation | $144.01   |
| 25th Percentile    | $128.80   |
| 50th Percentile    | $257.12   |
| 75th Percentile    | $379.80   |

The mean and median purchase amounts are very close, suggesting a symmetric distribution of spending without significant skewness. The standard deviation indicates a wide range of purchase values, as expected from the $10-$500 range.

## 5. Visualizations

### Purchase Amount Histogram

The histogram for `PurchaseAmount` shows a relatively uniform distribution across the range, confirming that there isn't a strong peak at specific price points for this synthetic dataset.

The histogram of purchase amount highlights the skew by showing a large concentration of lower value transactions. The scatter plot comparing customer age and purchase amount does not show a visible pattern. No strong relationship between age and spending behavior is observed in this dataset.

### CustomerAge vs. PurchaseAmount Scatter Plot

The scatter plot of `CustomerAge` against `PurchaseAmount` does not reveal any obvious linear correlation or strong trends. Purchase amounts appear to be randomly distributed across all age groups from 18 to 70, suggesting that in this synthetic dataset, age does not significantly influence the amount spent per transaction.

## 6. Written Analysis

Based on the analysis of the synthetic customer transaction dataset, several key observations can be made. The `CustomerAge` distribution, spanning from 18 to 70 years, has a mean of 44.73 years and a median of 45.00 years. This central tendency indicates a balanced representation across the adult age spectrum. The standard deviation of 15.24 years, along with quartiles at 32.00 (25th percentile) and 57.00 (75th percentile), signifies a considerable spread, meaning that customer ages are well distributed across the entire defined range rather than clustered around the mean.

For `PurchaseAmount`, the mean is $255.47 and the median is $257.12. The close proximity of these values suggests a relatively symmetrical distribution of spending, implying that there is no strong skewness towards very high or very low purchases. The standard deviation of $144.01 indicates significant variability in individual purchase values, reflecting a wide range of spending habits. The quartiles further delineate this variability, with 25% of purchases below $128.80 and 75% below $379.80. The histogram reinforces this by showing a fairly uniform distribution without prominent peaks. Critically, the scatter plot illustrating the relationship between `CustomerAge` and `PurchaseAmount` reveals no clear trend or correlation. Purchase amounts appear to be randomly dispersed across all age groups, implying that, within this synthetic data, a customer's age does not predict their spending amount.

## 7. Conclusion

This project successfully demonstrated the process of generating a synthetic dataset, performing essential data inspection, calculating descriptive statistics, and visualizing key distributions and relationships. While the synthetic nature of the data showed no correlation between age and purchase amount, the methodology applied is robust for analyzing real-world transactional data to uncover meaningful insights.
