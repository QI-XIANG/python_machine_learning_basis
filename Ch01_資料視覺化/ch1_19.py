#設定繪圖區間
import matplotlib.pyplot as plt

xpt = list(range(1,101)) #建立1~100系列的x坐標
ypt = [x**2 for x in xpt] #以x的平方建立y坐標

plt.axis([0, 100, 0, 10000]) #設定坐標軸的繪製區間
plt.scatter(xpt, ypt, color=(0, 1, 0))
plt.show()