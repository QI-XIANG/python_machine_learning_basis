#可以使用Sympy來繪製座標圖
#Smypy的plot()函數背後其實就是Matplotlib
#可以省略show()函數顯示座標圖
from sympy import *
from sympy.plotting import plot

x = Symbol('x')
#可以設定x軸的繪圖區間 #增加圖標題與軸標題
plot(2*x-5, (x, -5, 5), title="Sympy", xlabel="x", ylabel="2x-5") 
