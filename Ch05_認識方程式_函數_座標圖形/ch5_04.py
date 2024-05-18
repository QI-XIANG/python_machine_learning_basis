import matplotlib.pyplot as plt

x = [x for x in range(0,11)] # x = 0,1,2,3,4,5,6,7,8,9,10
y = [2 * y for y in x] # y = 2x
plt.xticks(x) # x軸刻度
plt.axis([0, 10, 0, 20]) #設定座標軸範圍
plt.plot(x, y) #繪製圖形
plt.grid() #添加網格
plt.show() #顯示圖形
