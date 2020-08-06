# using replace

import pandas as pd
import numpy as np

data = pd.read_csv("employees.csv")

#replace the missing value with -99
data.replace(np.nan,-99,inplace=True)
'''
#replacing the gender only with -99
data["Gender"].replace(np.nan,-99,inplace=True)
'''
print(data)

# Using interpolate() to find the missing values using linear method

data1 = {
        "A":[12, np.nan,np.nan,14],
         "B":[4,10,np.nan,18],
         "C":[12,np.nan,np.nan,16],
         "D":[12,10,17,np.nan]
         }

df = pd.DataFrame(data1)

# interpolate the missing values using linear method
df.interpolate(method='linear',limit_direction='forward',inplace=True)
print(df)

