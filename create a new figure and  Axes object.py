import matplotlib.pyplot as plt
import numpy as np

# create an array of 100 evenly spaced points  between 0 and 10
x = np.linspace(0, 10, 100)
y = np.sin(x)  # calculates the sine of each x values

ax = plt.subplots()

# plot the data as a line with read color ,solid line style and a linewidth of 2

ax.plot(x, y, color='red', linestyle='-', linewidth=2)

# Set the title , x - axix label and y-axis label
ax.set_title('Sine Wave')  # set the title of the plot
ax.set_xlabel('x-axis')  # set the label for the x-axis
ax.set_ylabel('y-axis')  # set the label for the x - axis


plt.show()
