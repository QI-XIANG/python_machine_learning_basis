#用Sympy模組->解一元二次方程式
from sympy import *

x = Symbol('x')
eq = x**2 + 5*x
result = solve(eq) #解方程式 x**2 + 5*x = 0
print(result) #以串列方式印出解答

