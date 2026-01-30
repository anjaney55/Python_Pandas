#selecting a column from a dataframe and filtering the data based on a condition
#using square brackets
#syntax: df['column_name']

import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Diana", "Eve", "Frank", "Grace","Hannah"],
    "Age": [28, 24, 35, 32, 29, 40, 22, 30],
    "salary": [50000, 60000, 55000, 70000, 48000, 80000, 52000, 62000],
    "performance": [85, 90, 78, 88, 92, 95, 80, 87]
}

df = pd.DataFrame(data)

# Selecting the 'Name' column
selected_column = df['Name']
print("Selected Column\n:")
print(selected_column)


# Filtering the DataFrame where 'Age' is greater than 30
filtered_data = df[df['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data)

#using AND operator to filter data based on multiple conditions
filtered_and = df[(df['Age'] >30) & (df['salary'] >60000)]
print("\nFiltered Data using And operator")
print(filtered_and)

#using OR operator to filter data based on multiple conditions
filtered_or = df[(df['Age'] >30) | (df['salary'] > 60000)]
print("\nFiltered Data using OR operator")
print(filtered_or) 

