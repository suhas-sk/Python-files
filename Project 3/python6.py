#Pie chart
from matplotlib import pyplot as plt

#defining labels
activities = ['eat', 'sleep', 'work', 'pubg']

#portion covered by each label
slices = [3,4,7,9]

#color for each labe;
colors = ['red', 'green', 'yellow', 'blue']

#plotting the pie chart
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0,0,0.1,0),radius=1.1, autopct='%1.2f%%')

#plotting legend
plt.legend()

#showing the plot
plt.show()

#shadow-gives the shadow if set to true
#startangle-rotates the angle from X-axis in anti-clockwise direction
#explode-explodes 1 or 2 slices of the pie chart
#autopct=Auto percentage is used to format the value of each label can display decimal values upto n places
