import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Diana", "Eve", "Frank", "Grace","Hannah"],
    "Age": [28, 24, 35, 32, 29, 40, 22, 30],
    "salary": [50000, 60000, 55000, 70000, 48000, 80000, 52000, 62000],
    "performance": [85, 90, 78, 88, 92, 95, 80, 87]
}

df = pd.DataFrame(data)

print(df.info())

# Using describe() method it show the statistical information of dataset

print('using describe() method')

print(df.describe())