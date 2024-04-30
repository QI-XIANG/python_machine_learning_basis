#可以使用Sympy來繪製座標圖
#Smypy的plot()函數背後其實就是Matplotlib
#可以省略show()函數顯示座標圖
from sympy import *
from sympy.plotting import plot

x = Symbol('x')
line = plot(2*x-5, 3*x-2, show=False) #可以繪製多函式圖形的座標圖
line[1].line_color = 'r' #設定第二條函式圖形的顏色
line.show() #顯示座標圖