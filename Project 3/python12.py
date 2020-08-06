# Stripplot using built-in dataset
# Using 'IRIS' dataset

import matplotlib.pyplot as plt
import seaborn as sns

# setting style to use
sns.set_style('dark')

#loading dataset
iris = sns.load_dataset('iris')

print(iris)

#decising the attributes of the dataset is to be plot
sns.stripplot(x='species', y='sepal_length', data=iris)

# giving title to the graph
plt.title('IRIS Flower')

#function to show the plot
plt.show()