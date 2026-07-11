import pandas as pd

print(pd.__version__)   # This will print the version of the pandas library

#  Pandas Main Data Structures:
# 1. Series: It is a one-dimensional array-like object that can hold any data type.
# 2. DataFrame: It is a two-dimensional tabular data structure that can hold any data type.

# Creating a Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)
print("Type of the Series:", type(s))
print("Index of the Series:", s.index)
print("Values of the Series:", s.values)
print("Head of the Series:", s.head())
print("Tail of the Series:", s.tail())
print("Shape of the Series:", s.shape)
print("Size of the Series:", s.size)
print("Type of the Series:", s.dtype)
print("Description of the Series:", s.describe())
print("Info of the Series:", s.info())

# Creating a Custom Index for the Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
print("Index of the Series:", s.index)
print("Values of the Series:", s.values)
print("Head of the Series:", s.head())
print("Tail of the Series:", s.tail())
print("Shape of the Series:", s.shape)
print("Size of the Series:", s.size)
print("Type of the Series:", s.dtype)
print("Description of the Series:", s.describe())
print("Info of the Series:", s.info())

# Creating a Series using dictionary
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390,
    "day4": 400,
    "day5": 410,
    "day6": 420,
    "day7": 430,
}
s = pd.Series(calories)
print(s)
print("Index of the Series:", s.index)
print("Values of the Series:", s.values)

# Create a DataFrame using a dictionary
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.index = ['a', 'b', 'c']
print(df)
print("Index of the DataFrame:", df.index)
print("Columns of the DataFrame:", df.columns)
print("Values of the DataFrame:", df.values)
print("Head of the DataFrame:", df.head())
print("Tail of the DataFrame:", df.tail())
print("Shape of the DataFrame:", df.shape)
print("Size of the DataFrame:", df.size)
print("Description of the DataFrame:", df.describe())
print("Info of the DataFrame:", df.info())

# Locate Row in DataFrame
# print(df.loc[0])
# print(df.loc[[0, 1]])
# print(df.loc[0:1])
# print(df.loc[[True, False, True]])
# print(df.loc[df['age'] > 30])
# print(df.loc[df['age'] > 30, ['name', 'city']])
# print(df.loc[df['age'] > 30, ['name', 'city']])