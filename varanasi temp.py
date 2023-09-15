import matplotlib.pyplot as plt
import numpy as np
bar_width = 0.35
temp = [32, 33, 36, 35, 35, 34, 1]
date = [9, 10, 11, 12, 13, 14, 15]
min = [26, 27, 24, 29, 31, 24, 25]
# y=[x*x for x in x][::-1]
# plt.plot(x,y)
plt.title("last week temp in Varanasi")
plt.xlabel("date")
plt.ylabel("tempature")


# plt.scatter(x,,color='Green', label='Set 1')
bar_width = 0.35
plt.plot(date, min)
plt.plot(date, temp)
plt.bar(date, min, color='red', alpha=0.5,
        edgecolor='black', linewidth=2, width=bar_width)
plt.bar(date, temp, color='green', alpha=0.5, edgecolor='black',
        linewidth=2, width=bar_width, bottom=date)
plt.grid(True)
plt.legend(['Temp', 'date', 'min'])

# for i,(x1,y2) in enumerate(zip(x,y)):
#     plt.text(i-bar_width/2,x1+1,str(x1),ha='center', fontweight='bold')
#     plt.text(i-bar_width/2,y2+1,str(y2),ha='center', fontweight='bold')

plt.savefig("varanasitemp.png")
plt.show()
