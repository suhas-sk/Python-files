# distplot
# using 'tips' dataset

import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
df = sns.load_dataset('tips')

'''
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
'''

#first five entries of dataset
df.head()

# distplot(a['any column'],kde=True or False, rug, hist, fit)
sns.set_style('whitegrid')
sns.distplot(df['total_bill'],kde=True, color='blue',bins=30,)

sns.jointplot(x='tip', y='total_bill',color='red', data=df,kind='scatter',)

# function to show the plot
plt.show()