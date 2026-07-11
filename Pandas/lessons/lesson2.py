# Reading and Writing Data
import pandas as pd

df = pd.read_csv('../data/students.csv')

print(df)

# View the first 5 rows of the DataFrame
print("View the first 5 rows of the DataFrame: \n", df.head())
# View the first 2 rows of the DataFrame
print("View the first 2 rows of the DataFrame: \n", df.head(2))

# View the last 5 rows of the DataFrame
print("View the last 5 rows of the DataFrame: \n", df.tail())
# View the last 2 rows of the DataFrame
print("View the last 2 rows of the DataFrame: \n", df.tail(2))

# Read only certain columns
print("Read only certain columns: \n", df[['Name', 'City']])
# or
df = pd.read_csv('../data/students.csv', usecols=['Name', 'Age'])
print("Read only certain columns: \n", df)

# Read Limited Rows from the DataFrame
print("Read Limited Rows from the DataFrame: \n", df.head(2))
df = pd.read_csv('../data/students.csv', nrows=2)
print("Read Limited Rows from the DataFrame: \n", df)

# File Without Headers
df = pd.read_csv('../data/students.csv', header=None)
print("File Without Headers: \n", df)

# Give Your Own Column Names
df = pd.read_csv('../data/students.csv', names=['N', 'A', 'M', 'C'])
print("Give Your Own Column Names: \n", df)

# Read JSON File
df = pd.read_json('../data/products.json')
print("Read JSON File: \n", df)

# Writing to a CSV File
data = {
    "Product Name": ["Apple", "Banana", "Cherry"],
    "Price": [100, 200, 300],
    "Quantity": [10, 20, 30],
    "Total": [1000, 2000, 3000],
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03"],
    "Time": ["10:00:00", "11:00:00", "12:00:00"],
    "Location": ["New York", "Los Angeles", "Chicago"],
    "Category": ["Fruit", "Fruit", "Fruit"],
    "Subcategory": ["Apple", "Banana", "Cherry"],
}

df = pd.DataFrame(data)
df.to_csv('../data/products.csv', index=False)
print("Writing to a CSV File: \n", df)


df.to_excel('../data/products.xlsx', index=False)
print("Writing to a Excel File: \n", df)


# Practice Exercise:

employees_data = {
    "e_name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "w_hours": [8, 8, 8, 8, 10],
    "w_shift": ["Day", "Day", "Day", "Day", "Night"],
}

df = pd.DataFrame(employees_data)
print(df)

df.to_csv("../data/employees.csv", header=None, index=False)
print("Writing to a CSV File: \n", df)

df = pd.read_csv("../data/employees.csv", header=None, names=["employee_name", "working_hours", "working_shift"])
print("Reading from a CSV File: \n", df)

# Mini Challenge:
sales_data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Speaker"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "price": [1000, 100, 150, 200, 50],
    "quantity": [10, 20, 30, 40, 50],
}

df = pd.DataFrame(sales_data)

df.to_csv("../data/sales.csv", index=False)
# Reads the file:
df = pd.read_csv("../data/sales.csv")
print("Sales Data: \n", df)

# Prints the first three rows
print("First three rows: \n", df.head(3))

# Reads only the Product and Price columns
df = pd.read_csv("../data/sales.csv", usecols=["product", "price"])
print("Read only the Product and Price columns: \n", df)