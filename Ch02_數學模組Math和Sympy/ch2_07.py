import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500) #建立含有500個元素的陣列
ypt1 = np.sin(xpt) #可以改用math.sin(xpt)
ypt2 = np.cos(xpt) #可以改用math.cos(xpt)

plt.plot(xpt, ypt1, label='sin') #使用預設顏色
plt.plot(xpt, ypt2, label='cos') #使用預設顏色

plt.xlabel("red")
plt.ylabel("value")

plt.title("Sin and Cos function")
plt.grid()

plt.legend(loc="best")
plt.show()
