import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10, 12]
y = [-x*x for x in x][::-1]
plt.scatter(x, y)
plt.plot(x, y)
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Second Degree Curve")
plt.show()
