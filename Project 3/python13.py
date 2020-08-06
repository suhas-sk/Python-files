# plotting using swarmplot
# Swarmplot is same as Stripplot but it does not overlpas points
# Can be used with Violin plot

import matplotlib.pyplot as plt
import seaborn as sns

# set style to use
sns.set_style('whitegrid')

# load the dataset
iris = sns.load_dataset('iris')

print(iris)

# use swarm plot
sns.violinplot(x='species', y='sepal_length', data=iris)
sns.swarmplot(x='species', y='sepal_length', color='black', data=iris)


# giving title to graph
plt.title('ViolinPlot and Swarmplot')

# function to show the plot
plt.show()


