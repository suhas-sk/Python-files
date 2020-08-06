# Using dropna() and interpolate() on csv files

import pandas as pd
import numpy as np

data1 = pd.read_csv("employees.csv")

'''
#dropping rows having all nan values
data1.dropna(how='all',inplace=True)
'''

'''
#dropping rows having atleast one nan values
data1.dropna(axis=0,how='any',inplace=True)
'''

'''
#dropping columns having atleast one  nan value
data1.dropna(axis=1,inplace=True)
'''

data1.interpolate(method='linear',direction='forward',inplace=True)
data1["Gender"].replace(to_replace=np.nan,value="No Gender",inplace=True)
data1["Team"].replace(to_replace=np.nan,value="No Team",inplace=True)


print(data1[10:29])
