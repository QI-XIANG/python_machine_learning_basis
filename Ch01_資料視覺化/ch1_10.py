import matplotlib.pyplot as plt

#繪製多組資料數據的線條
#調整線條色彩與樣式
data1 = [1, 2, 3, 4, 5, 6, 7, 8]
data2 = [1, 4, 9, 16, 25, 36, 49, 64]
data3 = [1, 3, 6, 10, 15, 21, 28, 36]
data4 = [1, 7, 15, 26, 40, 57, 77, 100]

seq = [1, 2, 3, 4, 5, 6, 7, 8]
#沒有設定顏色，系統會自動指定顏色
plt.plot(seq, data1, '-*' , seq, data2, '-o', seq, data3, '-^', seq, data4, '-s') #指定x和y座標
plt.title("Test Chart", fontsize=24) #設定圖表的標題，調整文字大小
plt.xlabel("x-Value", fontsize=14) #設定圖表的x軸座標，調整文字大小
plt.ylabel("y-Value", fontsize=14) #設定圖表的y軸座標，調整文字大小

plt.tick_params(axis='both', labelsize=12, color="red") #調整刻度的顏色和大小
plt.show()