#用Sympy模組->解一元一次方程式
from sympy import *

x = Symbol('x')
eq = 3*x + 5 -8
result = solve(eq) #解方程式
print(result) #以串列方式印出解答