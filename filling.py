import pandas as pd

data = {
    "Name": ["John", None, "Bob", "Diana", "Eve", "Frank", "Grace","Hannah"],
    "Age": [28, None, 35, 32, 29, 40, 22, 30],
    "salary": [50000, None, 55000, 70000, 48000, 80000, 52000, 62000],
    "performance": [85, None, 78, 88, 92, 95, 80, 87]
}

df = pd.DataFrame(data)
print(df)

#we can set the default vallue for missing Data usinf fillna() method
print("\nFillna() method\n")
df.fillna(0,inplace = True)
print(df)