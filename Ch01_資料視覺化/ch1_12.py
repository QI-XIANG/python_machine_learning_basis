import matplotlib.pyplot as plt

#繪製多組資料數據的線條
#調整線條色彩與樣式
Benz = [3367, 4120, 5539]
BMW = [4000, 3590, 4423]
Lexus = [5200, 4930, 5350]

seq = [2021, 2022, 2023]
plt.xticks(seq) #自行設定刻度
plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^') #指定x和y座標
plt.title("Sales Report", fontsize=24) #設定圖表的標題，調整文字大小
plt.xlabel("Year", fontsize=14) #設定圖表的x軸座標，調整文字大小
plt.ylabel("Number of Sales", fontsize=14) #設定圖表的y軸座標，調整文字大小

plt.tick_params(axis='both', labelsize=12, color="red") #調整刻度的顏色和大小
plt.show()