"""
#Handling missing data in pandas
#isnull
#notnull
#dropna
#fillna
#replace
#interpolate
"""

#Checking for isnull and notnull
import pandas as pd
import numpy as np

#creating a dataframe
data = {"First Score": [100,90,np.nan,80],
      "Second Score": [20,60,44,np.nan],
      "Third Score": [np.nan,np.nan,70,80]}
df = pd.DataFrame(data)
print(df)

#using isnull() function
print(df.isnull())
#isnull()-returns True when it finds 'Nan' value

#using notnull
print(df.notnull())
#notnull()-returns False when it finds 'Nan' value

