#Line Plotting in Python

from matplotlib import pyplot as plt
import  cv2

#X-axis values
# [x1, x2, x3, x4, x5]
x = [1, 2, 5, 6, 8]

#Y-axis values
#  [y1, y2, y3, y4 ,y5]
y = [2, 4, 5, 7, 0]

#Function to plot
plt.plot(x, y, color = 'green')

#function to show the plot
plt.show()