#用Sympy模組->解聯立方程式
from sympy import *

x, y = symbols('x y')
eq1 = 3*x + 2*y - 6
eq2 = 9*x + y - 3
result = solve((eq1, eq2)) #解聯立方程式
print(result) #以字典方式印出解答

print(eq1.subs(result)) #代入解答驗證
print(eq2.subs(result)) #代入解答驗證