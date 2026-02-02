#using interpolate() method we fill none value with the trends using linearmethod
'''
1. timer series data
2. numeric data with trends
3. avoid droping rows
'''

import pandas as pd 

data = {
    "Time" : [1,2,3,4,5],
    "value" : [10,None,30,None,50]
}

df = pd.DataFrame(data)
print('\nBefore Interpolate\n')
print(df)

df['value'] = df['value'].interpolate(method='linear')
print('\n After Interpolate \n')
print(df)

