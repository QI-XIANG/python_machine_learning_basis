import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw=10) #調整線條的粗細
plt.title("Test Chart", fontsize=24) #設定圖表的標題，調整文字大小
plt.xlabel("Value", fontsize=16) #設定圖表的x軸座標，調整文字大小
plt.ylabel("Square", fontsize=16) #設定圖表的y軸座標，調整文字大小
plt.tick_params(axis='both', labelsize=12, color="red") #調整刻度的顏色和大小
plt.show()