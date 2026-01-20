import pandas as pd

df = pd.read_csv('sales_data_sample.csv', encoding='Latin1')

print("First 5 rows of the DataFrame:")
print(df.head(5)) # Display the first 5 rows of the DataFrame

print("\nLast 5 rows of the DataFrame:")
print(df.tail(5)) # Display the last 5 rows of the DataFrame