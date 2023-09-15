import matplotlib.pyplot as plt
import numpy as np

y=[32,33,36,35,35,34,32]
x=[9,10,11,12,13,14,15]
min=[26,27,24,29,31,24]
# y=[x*x for x in x][::-1]
# plt.plot(x,y)
plt.title("last week temp in Varanasi")
plt.xlabel("tempature")
plt.ylabel("Day")
plt.plot(x,y)

plt.scatter(x,y,color='Green')
plt.bar(x,y)
plt.grid(True)
plt.legend(['Temp','date'])
plt.savefig("varanasitemp.png")
plt.show()
