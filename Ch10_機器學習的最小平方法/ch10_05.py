import matplotlib.pyplot as plt
import numpy as np

x = np.array([22, 26, 23, 28, 27, 32, 30])
y = np.array([15, 35, 21, 62, 48, 101, 86])

a,b = np.polyfit(x, y, 1)
print("斜率 a = {0:5.2f}".format(a))
print("截距 b = {0:5.2f}".format(b))

y2 = a*x + b
plt.scatter(x, y)
plt.plot(x, y2)

sold = a*31 + b
print("氣溫31度時的銷量 = {}".format(int(sold)))
plt.plot(31, int(sold), '-o')
plt.grid()
plt.show()
