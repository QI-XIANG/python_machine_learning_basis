#繪製波形
import numpy as np
import matplotlib.pyplot as plt

xpt = np.linspace(0, 10, 500) #建立含有500個元素的串列
ypt1 = np.sin(xpt)
ypt2 = np.cos(xpt)

plt.scatter(xpt, ypt1, color=(0, 1, 0)) #綠色
plt.scatter(xpt, ypt2)

plt.show()