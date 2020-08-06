#Bar Graph plotting for discrete values
from matplotlib import pyplot as plt

#X-axis values
x = [1, 3, 4, 5, 6]

#Y-axis values
y = [1, 5, 9, 12, 8]

#Function to plot the bar
plt.bar(x, y, width=0.8, color  = ['red', 'green'])

#naming X-axis
plt.xlabel('X-axis')

#naming Y-axis
plt.ylabel('Y-axis')

#naming the Chart/Graph
plt.title('My Bar Graph!')

#function to show the graph
plt.show()