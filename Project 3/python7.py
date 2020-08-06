#Plotting cuvres of given equation
#plotting Sine curve

import matplotlib.pyplot as plt
import numpy as np

#setting the x-coordinates
x = np.arange(0,2*(np.pi), 0.1)   # Range is 0 to 2*3.142

#setting the y-coordinates
y = np.sin(x)

#plotting the curve
plt.plot(x,y)

#showing the curve
plt.show()
