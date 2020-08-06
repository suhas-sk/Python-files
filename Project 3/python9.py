#Plotting 2D curves
#Drawing sin,cos curves

from matplotlib import pyplot as plt
import numpy as np

def create_plot(ptype):
    # setting x-axis values
    x = np.arange(0, 5, 0.01)

    # setting y-axis values
    if ptype == 'sin':
        y = np.sin(2*np.pi*x)
    elif ptype == 'cos':
        y = np.cos(2*np.pi*x)

    return (x, y)


# setting a style to use
plt.style.use('ggplot')

# defining subplots and their positions
plt1 = plt.subplot2grid((11, 1), (0, 0), rowspan=4, colspan=1)
plt2 = plt.subplot2grid((11, 1), (6, 0), rowspan=4, colspan=1)

# plotting points on each subplot
x, y = create_plot('sin')
plt1.plot(x, y, label='sine wave', color='b')

x, y = create_plot('cos')
plt2.plot(x, y, label='cosine wave', color='g')


# showing legends
plt1.legend()
plt2.legend()


# function to show the plot
plt.show()