'''
#dropna
thresh-pass the count of nan values in a row  it will drop the  rows having the count
axis-pass the count of nan values in a row  it will drop the  columns having the count
how- if set to any then drops the row having atleast one nan value

'''
import pandas as pd
import numpy as np


data = {
        "First Score": [100,81,92,80],
        "Second Score": [20,np.nan,44,np.nan],
        "Third Score": [88,np.nan,70,80],
        "Fourth Score":[50,np.nan,98,99],
        "Fifth Score":[80,np.nan,np.nan,np.nan,]
        }

new_df = pd.DataFrame(data)
'''
#dropping rows having only one nan values
new_df.dropna(thresh=1,inplace=True)
'''

'''
#dropping rows having two nan values
new_df.dropna(thresh=2,inplace=True)
'''

'''
#dropping rows having atleast one nan value
new_df.dropna(how='all',inplace=True)
'''

'''
# dropping columns with atleast 1 nan value
new_df.dropna(axis=1,inplace=True)
'''

#dropping rows having atleast one nan value
new_df.dropna(axis=0,how='any',inplace=True)

print(new_df)
