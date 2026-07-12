# Adding, Updating, Renaming, and Deleting Data

import pandas as pd
import numpy as np

df = pd.read_csv("E:\Learn Pandas\data\students.csv")
print(df)

# 1. Adding a New Column:
df["Section"] = "A"
print(df)

# 2. Adding Values from a List
df["Grade"] = [
    "B",
    "A",
    "C",
    "B",
    "A",
    "B",
    "B",
    "C",
    "A",
    "B"
]
print(df)

# 3. Creating Calculated Columns
df["Percentage"] = df["Marks"] / 100
print(df)

# Using Conditions with np.where()
# Syntax: np.where(condition, value_if_true, value_if_false)
df["Result"] = np.where(
    df["Marks"] >= 80,
    "Pass",
    "Fail"
)
print(df)

# 5. Updating Existing Values
df["Age"] += 5
print(df)

# 6. Update Selected Rows
df.loc[df["Name"] == "Alice", "Marks"] += 10
print(df)

# 7. Rename Columns
df.rename(columns={"Marks": "Score"}, inplace=True)
print(df)

# Rename multiple columns:
df.rename(columns={
    "Age": "Student Age",
    "Score": "Student Score"
}, inplace=True)
print(df)

# 9. Delete a Column
df.drop(columns=["Section"], inplace=True)
print(df)

del df["Grade"]
print(df)

df.pop("Percentage")
print(df)

# 10. Delete Rows -> done using index
df.drop(index=[0, 1, 2], inplace=True)
print(df)

# 11. Insert a Column at a Specific Position
df.insert(
    1,
    "Roll no.",
    [1, 2, 3, 4, 5, 6, 7]
)
print(df)

print(df.columns)
print(df.index)