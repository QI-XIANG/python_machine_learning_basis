#圖表顯示中文
#繪製多組資料數據的線條
#調整線條色彩與樣式
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', family='Microsoft JhengHei')

Benz = [3367, 4120, 5539]
BMW = [4000, 3590, 4423]
Lexus = [5200, 4930, 5350]

seq = [2021, 2022, 2023]
plt.xticks(seq) #自行設定刻度

plt.plot(seq, Benz, '-*', label="Benz") #指定x和y座標
plt.plot(seq, BMW, '-o', label="BMW")
plt.plot(seq, Lexus, '-^', label="Lexus")

plt.legend(loc='best') #新增圖表的圖例

plt.title(u"銷售報表", fontsize=24) #設定圖表的標題，調整文字大小
plt.xlabel(u"年度", fontsize=16) #設定圖表的x軸座標，調整文字大小
plt.ylabel(u"銷售量", fontsize=16) #設定圖表的y軸座標，調整文字大小

plt.tick_params(axis='both', labelsize=12, color="red") #調整刻度的顏色和大小
plt.show()

#中文部分取自: https://dev.to/codemee/matplotlib-xian-shi-zhong-wen-4998