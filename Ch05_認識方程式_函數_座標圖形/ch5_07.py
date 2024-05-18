import matplotlib.pyplot as plt

x = [x for x in range(0,11)]
y1 = [2 * y for y in x] # y = 2x
y2 = [3 * y  + 2 for y in x] # y = 3x+2
y3 = [4 * y -  3 for y in x] # y = 4x-3

plt.xticks(x)
plt.plot(x, y1, label='L1') #繪製圖形
plt.plot(x, y2, label='L2') #繪製圖形
plt.plot(x, y3, label='L3') #繪製圖形
plt.legend(loc='best') #添加圖例
plt.grid() #添加網格
plt.show() #顯示圖形