#Histogram plotting for continuous variables
from matplotlib import pyplot as plt

#frequencies
ages = [10, 20, 30, 30, 56, 70, 82, 83, 87, 12, 27, 47, 91, 99, 34]

#setting the ranges
range = (0, 100)

#setting the interval
bins = 10

#naming X-axis
plt.xlabel('Age')

#naming frequency label
plt.ylabel('No. of People')

#title
plt.title('My Histogram')

#function to plot histogram
plt.hist(ages, bins, range, rwidth=0.6, color='green', histtype='bar')

#function to show histogram
plt.show()