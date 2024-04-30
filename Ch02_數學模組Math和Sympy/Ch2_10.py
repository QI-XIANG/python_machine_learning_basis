#將字串轉換為數學表達式
from sympy import *

x = Symbol('x')
eq = input("請輸入公式:") #注意，這邊沒有偵錯功能，輸入錯誤會直接報錯
eq = sympify(eq) #將字串轉換為數學表達式
print(eq)
result = eq.subs({x: 1})
print(result)