#Plotting 2D curves advanced

from matplotlib import pyplot as plt
import numpy as np
from math import *
#function to generate points
def create_plot(ptype):
    #setting the x-axis values
    x = np.arange(-1, 1, 0.01)


    #setting the y-axis values
    if ptype == 'para1':
        y = x**2
    elif ptype == 'para2':
        y=-x**2
    '''
    elif ptype == 'para3':
        y = x**0.5
    elif ptype == 'para4':
        y = -x**0.5
'''

    return (x,y)

def create_plot_1(ptype):
    #setting y values
    y = np.arange(-1, 1, 0.01)

    #setting x values
    if ptype == 'para3':
        x = y**2
    elif ptype == 'para4':
        x = -y**2

    return (x,y)


#setting a style to use
plt.style.use('fivethirtyeight')

#create a figure
fig = plt.figure()

#define subplots and their positions in figures
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)

#plotting points on each subplot
x,y = create_plot('para1')
plt1.plot(x, y , color = 'r')
plt1.set_title('$y=x^2$')

x,y = create_plot('para2')
plt2.plot(x, y, color = 'g')
plt2.set_title('$y=-x^2$')


x,y = create_plot_1('para3')
plt3.plot(x, y , color = 'b')
plt3.set_title('$x=y^2$')

x,y = create_plot_1('para4')
plt4.plot(x, y , color='purple')
plt4.set_title('$x=-y^2$')

#adjusting space between the subplots
fig.subplots_adjust(hspace=0.6,wspace=0.6)

#function to show the plot
plt.show()
