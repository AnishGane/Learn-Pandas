# Missing Data (Data Cleaning)
import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, np.nan, 19, 22],
    "Marks": [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)

print(df)

# 1. Detect Missing Values
print(df.isnull())

# 2. Opposite: notnull()
print(df.notnull())

# 3. Count Missing Values
print(df.isnull().sum())

# 4. Total Missing Values
print(df.isnull().sum().sum())

# 5. Remove Missing Rows
# df.dropna(inplace=True)
# print(df)

# 6. Remove Missing Columns
# df.dropna(axis=1, inplace=True)
# print(df)

# 7. Fill Missing Values
# df.fillna(0, inplace=True)
# print(df)

# 8. Fill Numeric Columns
df["Age"] = df["Age"].fillna(
    df["Age"].mean(), inplace=True
)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].median(), inplace=True
)
print(df)

# 9. Forward Fill
df.ffill()

# 10. Backward Fill
df.bfill()

# 11. Replace Specific Values
df.replace(np.nan, 0, inplace=True)

df.replace({
    "Age": np.nan,
    "Marks": np.nan
})

# 12. Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# 13. Find Duplicate Rows
df.duplicated()