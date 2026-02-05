'''missing Data will represet in 2 ways
1. NaN - Not a Number
2. None - for object data type

for finding the missing data we use
isnull() method 
it gives
True - NaN is missing
False - value is present'''

import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Diana", "Eve", "Frank", "Grace","Hannah"],
    "Age": [28, 24, None, 32, 29, 40, 22, 30],
    "salary": [50000, 60000, 55000, 70000, 48000, 80000, 52000, 62000],
    "performance": [85, 90, 78, 88, 92, None, 80, 87]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())