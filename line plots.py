import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[2,4,6,8,10]
y=[x*x for x in x][::-1]
plt.plot(x,y)
plt.xlabel(x)
plt.ylabel(y)
plt.show()
