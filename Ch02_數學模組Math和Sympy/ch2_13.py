#用Sympy模組->解含未知數的方程式
from sympy import *

x, a, b, c = symbols('x a b c')
eq = a*x*x + b*x + c
result = solve(eq, x) #解方程式 a*x*x + b*x + c = 0, 第2個參數是要解的未知數
print(result) #以串列方式印出解答