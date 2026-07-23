# Statistical Operations & Descriptive Analysis

import pandas as pd

df = pd.read_csv("E:\Learn Pandas\data\students.csv")
# print(df)

# describe()

print(f"Describe: \n {df.describe()}")
print(f"Describe all: \n {df.describe(include='all')}")

# 1. count()
print(f"Count: \n {df.count()}")
print(f"Count of Name: {df['Name'].count()}")

# 2. mean()
print(f"Mean of Marks: {df['Marks'].mean()}")

# 3. median()
print(f"Median of Marks: {df['Marks'].median()}")

# 4. mode()
print("Mode of Marks: \n", df['Marks'].mode())

# 5. sum()
print(f"Sum of Marks: {df['Marks'].sum()}")

# 6. min()
print(f"Min of Marks: {df['Marks'].min()}")

# 7. max()
print(f"Max of Marks: {df['Marks'].max()}")

# 8. std() -> Shows how spread out the data is. Low Spread = Less Variation/Low Standard Deviation and vice versa
print(f"Standard Deviation of Marks: {df['Marks'].std()}")

# 9. var() -> Variance is the average of the squared differences between the mean and each data point. (std^2 = var)
print(f"Variance of Marks: {df['Marks'].var()}")

# 10. Quantiles
print(f"Quantile 0.25: {df['Marks'].quantile(0.25)}")
print(f"Quantile 0.5: {df['Marks'].quantile(0.5)}")
print(f"Quantile 0.75: {df['Marks'].quantile(0.75)}")
print(f"Quantile 0.9: {df['Marks'].quantile(0.9)}")
print(f"Quantile 0.99: {df['Marks'].quantile(0.99)}")

# 11. Unique values
print(f"Unique values: {df['Marks'].unique()}")

# 12. number of unique values
print(f"Number of unique values: {df['Marks'].nunique()}")

# 13. Frequency count
print(f"Frquency count: {df['Marks'].value_counts()}")

# 14. Correlation
print("Corr of age and marks: \n", df[["Age", "Marks"]].corr())

# 15. aggregate multiple statistics
print("Aggregate multiple statistics: \n", df["Marks"].agg(["min", "max", "std", "idxmax", "idxmin"]))

# Round Result
print(f"Round of Marks: {df['Marks'].mean().round(2)}")