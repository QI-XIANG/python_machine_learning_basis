#用Sympy模組代入數字解決線性代數問題
from sympy import *

x = Symbol('x')
y = Symbol('y')
eq = 5 * x + 6 * y
result = eq.subs({x: 1, y: 2}) #代入x=1, y=2
print(result)