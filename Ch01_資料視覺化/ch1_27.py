#建立不等寬度的散佈圖
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 5, 500) #建立含500個元素的串列
ypt = 1 - 0.5 * np.abs(xpt - 2)
lwidths = (1 + xpt) ** 2 #寬度陣列

plt.scatter(xpt, ypt, s=50, c=ypt, cmap="hsv")
plt.show()