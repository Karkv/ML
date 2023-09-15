import matplotlib.pyplot as plt
import numpy as np

#GEnerate some random data

data=np.random.normal(size=10)

#create a histogram with 20 bins

plt.hist(data,bins=20)


# Add labels and titles

plt.title('Distribution of Random Data')
plt.xlabel('values')
plt.ylabel('frequency')

#Display the plot
plt.show()

