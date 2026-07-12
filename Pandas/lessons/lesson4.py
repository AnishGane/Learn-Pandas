# Sorting Data in Pandas
import pandas as pd
import numpy as np

df = pd.read_csv("E:\Learn Pandas\data\students.csv")

# 1. sort_values() -> This sorts rows based on one or more column values.
sorted_df = df.sort_values(by="Marks")
print(f"Sorted DataFrame: \n{sorted_df}\n\nOriginal DataFrame: \n{df}\n\nsorted_df)")

# Sort in Descending Order
sorted_df = df.sort_values(by="Marks", ascending=False)
print(f"Sorted DataFrame: \n{sorted_df}\n\nOriginal DataFrame: \n{df}\n\nsorted_df)")

# Sort by multiple columns
sorted_df = df.sort_values(by=["Marks", "Name"])
print(f"Sorted DataFrame: \n{sorted_df}\n\nOriginal DataFrame: \n{df}\n\nsorted_df)")

sorted_df = df.sort_values(by=["Age", "Marks"], ascending=[True, False])
print(f"Sorted DataFrame: \n{sorted_df}\n\nOriginal DataFrame: \n{df}\n\nsorted_df)")

df.loc[1, "Marks"] = np.nan
print(df)

# Sorting with Missing Values
sorted_df = df.sort_values(by="Marks", na_position="first")
print(f"Sorted DataFrame: \n{sorted_df}\n\nOriginal DataFrame: \n{df}\n\nsorted_df)")

# Stable Sorting -> This matters when equal values should keep their original order.
sorted_df = df.sort_values(by="Marks", kind="stable")
print(f"Sorted DataFrame: \n{sorted_df}\n\nOriginal DataFrame: \n{df}\n\nsorted_df)")

