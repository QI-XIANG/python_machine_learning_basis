#繪製一系列的黃色點
import matplotlib.pyplot as plt

xpt = list(range(1,101)) #建立1~100系列的x坐標
ypt = [x**2 for x in xpt] #以x的平方建立y坐標

plt.scatter(xpt, ypt, color="y")
plt.show()