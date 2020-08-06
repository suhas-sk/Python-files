#Scatter plotting
from matplotlib import pyplot as plt

#X-axis values
# [x1, x2, x3, x4, x5]
x = [1, 2, 5, 6, 8]

#Y-axis values
#  [y1, y2, y3, y4 ,y5]
y = [2, 4, 5, 7, 6]

#naming X-axis
plt.xlabel('X-axis')

#naming Y-axis
plt.ylabel('Y-axis')

#title
plt.title('My Scatter Plotting')

#function to plot the graph
plt.scatter(x, y, color='blue', label='stars', marker='*', s=30)

#plotting legend displays star '*' symbol in top corner
plt.legend()

#function to show the graph
plt.show()