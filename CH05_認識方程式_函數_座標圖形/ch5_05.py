import matplotlib.pyplot as plt

x = [x for x in range(0,11)] # x = 0,1,2,3,4,5,6,7,8,9,10
y1 = [2 * y for y in x] # y = 2x
y2 = [(2 * y - 2) for y in x] # y = 2x-2
y3 = [(2 * y + 2) for y in x] # y = 2x+2

plt.xticks(x) # x軸刻度
plt.plot(x, y1, label='y=L1') #繪製圖形
plt.plot(x, y2, label='y=L2') #繪製圖形
plt.plot(x, y3, label='y=L3') #繪製圖形

plt.grid() #添加網格
plt.legend(loc='best') #添加圖例
plt.show() #顯示圖形
