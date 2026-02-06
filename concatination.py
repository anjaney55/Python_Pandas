'''It should done in

Vertically(rows-wise)
Horizontally(column-wise)

Syntax :
   pd.concat([df1, df2], axis = 0, ignore_index = True)

axis=0 is rows and 1 is column'''

import pandas as pd

df_rigion1 = pd.DataFrame({
    'CID' : [1,2],
    'CName' :['Akash', 'Suresh']
}) 

df_rigion2 = pd.DataFrame({
    'CID' : [3,4],
    'CName' :['Manoj','Vikki']
})

#Concatination Vertically
Concate_data = pd.concat([df_rigion1, df_rigion2], axis = 1, ignore_index=True)

print(Concate_data)