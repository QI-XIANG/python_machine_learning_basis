import matplotlib.pyplot as plt

x = [x for x in range(0,11)] # x = 0,1,2,3,4,5,6,7,8,9,10
y1  = [2 * y for y in x]  # y1 = 2x
y2 = [3 * y for y in x]  # y2 = 3x
y3 = [4 * y for y in x]  # y3 = 4x

plt.xticks(x) # x軸刻度

plt.plot(x, y1, label='L1') #繪製圖形
plt.plot(x, y2, label='L2') #繪製圖形
plt.plot(x, y3, label='L3') #繪製圖形

plt.legend(loc='best') #添加圖例
plt.grid() #添加網格
plt.show() #顯示圖形