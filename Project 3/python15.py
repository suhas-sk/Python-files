"""
# Rugplot
It plots data in array sticks on an axis.
Just like distplot it takes single column, but instead of creating histogram it creates dashes all over the plots
If you comparee it joinplot , joinplot counts the dashes and  shows it as bins.
"""
import matplotlib.pyplot as plt
import seaborn as sns

# setting a style to use
sns.set_style('whitegrid')

# loading dataset
iris = sns.load_dataset('iris')

print(iris)

# plotting the petal_length
sns.rugplot(iris['petal_length'], color='b')

#givnig title to the plot
plt.title('Rugplot')

#fucntion to show the plot
plt.show()