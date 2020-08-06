# Pairplot Plotting
# Represents parwise relation across entire dataframe ans supports
# additional argument called 'hue' for categorical representation

import matplotlib.pyplot as plt
import seaborn as sns

# setting style to use
sns.set_style('darkgrid')
"""
More stlyes
#dark
#white
#whitegrid
"""

# loading IRIS flower dataset
iris = sns.load_dataset('iris')

print(iris)

# plotting the species along sepal and petals height and width
sns.pairplot(iris, hue='species', palette='muted')
"""
More color pallates
#muted
#dark
#colrblind
#pastel
#bright
#deep
"""


# function to show the plot
plt.show()