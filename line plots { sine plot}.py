import matplotlib.pyplot as plt
import json
import requests


import numpy as np
# simple plots
# Generate some data for the plot
url = ("https://gist.githubusercontent.com/Karkv/fd34b366c7e33d78d1227d59eb38f0dc/raw/4a1f46d7e97787a4fe01816a4ece98f3837971ad/mlgraph")
responce = requests.get(url)
data = responce.text
data = json.loads(data)
x = data["x"]
y = data["y"]

plt.plot(x, y)

plt.grid(True)


plt.scatter(x, y)
plt.show()
