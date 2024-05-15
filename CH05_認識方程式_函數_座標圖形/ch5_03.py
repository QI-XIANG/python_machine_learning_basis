import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 100) #產生0到1000之間的100個數字
y = 0.03 * x - 18 #計算y值
plt.axis([0, 1000, -20, 15]) #設定座標軸範圍
plt.plot(x, y, '-*') #繪製圖形
plt.xlabel("Customers") #x軸標籤
plt.ylabel("Profit") #y軸標籤
plt.grid() #添加網格
plt.show() #顯示圖形