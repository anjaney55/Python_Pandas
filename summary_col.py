#It gives the summary of the column
'''
we use sum(), mean() for average , max(), min() for minimum value in the column
'''

import pandas as pd 

data = {
    'Name' : ['Arun', 'Karun', 'Varun'],
    'Age' : [39,45,32],
    'salary' : [30000,27400,35490]

}

df = pd.DataFrame(data)

print(df)

avarage_salary = df['salary'].mean()
print(f'\navarage_salary : {avarage_salary}\n')

sum_salary = df['salary'].sum()
print(f'Sum of salary :{sum_salary}\n')

