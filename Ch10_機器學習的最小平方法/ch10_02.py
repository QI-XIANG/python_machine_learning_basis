import numpy as np

x = np.array([1, 2, 3])
y = np.array([5, 10, 20])

a,b = np.polyfit(x, y, 1)
print("斜率 a = {0:5.2f}".format(a))
print("截距 b = {0:5.2f}".format(b))