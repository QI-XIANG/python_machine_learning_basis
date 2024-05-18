import matplotlib.pyplot as plt
x = [x for x in range(0,11)]
y = [(3 * y - 18) for y in x]
plt.plot(x , y, '-*') #繪製圖形
plt.xlabel('Children') #x軸標籤
plt.ylabel('Apple') #y軸標籤
plt.grid() #添加網格
plt.show() #顯示圖形