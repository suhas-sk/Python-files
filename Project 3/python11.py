# Plotting categorical data
#plots with seaborn

import matplotlib.pyplot as plt
import seaborn as sns

# x-axis values
x = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

# y-axis values
y = [5, 6.4, 9.1, 7, 3.2, 5.9, 8.8]

# plotting strip plot with seaborn
ax = sns.stripplot(x, y, color='b', linewidth=0.8)

# giving labels to x-axis and y-axis
ax.set(xlabel='Days', ylabel='Amount spend')

#gving title to the plot
plt.title('My first Graph in Seaborn')

#function to show plot
plt.show()