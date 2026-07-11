# Filtering Data
import pandas as pd

df = pd.read_csv("../data/students.csv")

# Basic Filtering
# df[condition] -> The condition must return True or False for every row.

high_marks = df[df['Marks'] > 80]
print("High Marks: \n", high_marks)

res = df[(df['Age'] > 20) & (df['Marks'] > 80)]
print("Result: \n", res)

res = df[(df['Age'] > 20) | (df['Marks'] > 80)]
print("Result: \n", res)

# isin() -> Returns True if the value is in the list of values.
res = df[df['City'].isin(['Kathmandu', 'Pokhara'])]
print("Result: \n", res)

# between() -> Returns True if the value is between the two values.
res = df[df['Age'].between(20, 25)]
print("Result: \n", res)

# String Filtering
s = df[df['Name'].str.startswith('A')]
e = df[df['Name'].str.endswith('a')]
c = df[df['Name'].str.contains('a')]
i = df[df['Name'].str.contains('a', case=False)]
print("s: \n", s)
print("e: \n", e)
print("c: \n", c)
print("i: \n", i)

# Using query() method
res = df.query('Age > 20 and Marks > 80')
print("Result: \n", res)

# Selecting Specific Columns After Filtering
res = df.loc[df['Age'] > 20, ['Name', 'City']]
print("Result: \n", res)

# Practice Exercises

# 1. Show students older than 21.
res = df[df['Age'] > 21]
print("Age > 21: \n", res)

# 2. Show students with marks less than 80.
res = df[df['Marks'] < 80]
print("Marks < 80: \n", res)

# 3. Show students whose city is Kathmandu.
res = df[df['City'] == 'Kathmandu']
print("City == Kathmandu: \n", res)

# 4. Show students whose city is not Pokhara.
res = df[df['City'] != 'Pokhara']
print("City != Pokhara: \n", res)

# 5. Show students with marks between 80 and 90.
res = df[df['Marks'].between(80, 90)]
print("Marks between 80 and 90: \n", res)

# 6. Show students from Kathmandu or Butwal.
res = df[df['City'].isin(['Kathmandu', 'Butwal'])]
print("City in Kathmandu or Butwal: \n", res)

# 7
res = df[df['Name'].str.startswith('J')]
print("Name starts with J: \n", res)

# 8
res = df.loc[df["Marks"] > 90, ["Name", "City"]]
print("Marks > 90: \n", res)

# 9
count = len(df[df['Marks'] >= 85])
print("Number of students with marks >= 85: ", count)

# 10
q = df.query("Age > 20 & Marks > 85")
print("Query: \n", q)