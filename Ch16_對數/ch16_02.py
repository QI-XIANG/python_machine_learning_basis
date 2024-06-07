import matplotlib.pyplot as plt
import numpy as np 
import math

x1 = np.linspace(0.1, 10, 99)
x2 = np.linspace(0.1, 10, 99)
y1 = [math.log2(x) for x in x1]
y2 = [math.log(x, 0.5) for x in x2]

plt.plot(x1, y1, label="base = 2")
plt.plot(x2, y2, label="base = 0.5")

plt.legend(loc="best")
plt.axis([0, 10, -5, 5])
plt.grid()
plt.show()
