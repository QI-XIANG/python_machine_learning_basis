import matplotlib.pyplot as plt
import numpy as np

x2 = np.linspace(-3, 3, 30)
x4 = np.linspace(-3, 3, 30)
y2 = 2**x2
y4 = 4**x4

plt.plot(x2, y2, label='y=2**x')
plt.plot(x4, y4, label='y=4**x')
plt.plot(0, 1, '-o')
plt.legend(loc="best")
plt.axis([-3, 3, 0, 30])
plt.grid()
plt.show()