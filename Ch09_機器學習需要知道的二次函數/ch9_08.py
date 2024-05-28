import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)
y = x**3 - x
plt.plot(x, y)
plt.grid()
plt.show()
