import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw=10) #調整線條的粗細
plt.title("Test Chart") #設定圖表的標題
plt.xlabel("Value") #設定圖表的x軸座標
plt.ylabel("Square") #設定圖表的y軸座標
plt.show()