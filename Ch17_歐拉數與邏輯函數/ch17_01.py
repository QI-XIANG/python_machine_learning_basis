import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 1000, 100000)
y = [(1+1/x)**x for x in x]

plt.axis([0, 10, 0, 3])
plt.plot(x, y, label="Euler's Number")

plt.legend(loc="best")
plt.grid()
plt.show()