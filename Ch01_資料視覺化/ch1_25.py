#填滿區間shading regions
import matplotlib.pyplot as plt 
import numpy as np

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)

plt.plot(x, y)
plt.fill_between(x, -1, y, color="yellow", alpha=0.3)
plt.show()