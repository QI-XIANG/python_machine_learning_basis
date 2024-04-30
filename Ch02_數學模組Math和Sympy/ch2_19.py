#可以使用Sympy來繪製座標圖
#Smypy的plot()函數背後其實就是Matplotlib
#可以省略show()函數顯示座標圖
from sympy import *
from sympy.plotting import plot

x = Symbol('x')
plot(2*x-5, 3*x-2) #可以繪製多函式圖形的座標圖