import matplotlib.pyplot as plt

import numpy as np
#simple plots
# Generate some data for the plot

x=np.linspace(0,10,100) #Create as array of 100 evenly spaced points between 0 and 10

y=np.sin(x) 
plt.grid(True)


plt.scatter(x,y)
plt.show()