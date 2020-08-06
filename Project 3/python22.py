# using fillna
import pandas as pd
import numpy as np

data = {"First Score": [100,90,np.nan,80],
      "Second Score": [20,60,44,np.nan],
      "Third Score": [np.nan,np.nan,70,80]}

df = pd.DataFrame(data)


#filling missing value  with zero
'''
df = df.fillna(0)
print(df)
'''


#filling the missing value with the previous value
'''
df = df.fillna(method='pad')
print(df)
'''

# filling missing value with the next value
'''
df = df.fillna(method='bfill')
print(df)
'''

# Filling the null values in csv file
new_df = pd.read_csv("employees.csv")

'''
#printing few rows
print(new_df[10:24])
'''

#filling the missing gender values with 'no gender'
new_df["Gender"].fillna("No Gender",inplace=True)
print(new_df)