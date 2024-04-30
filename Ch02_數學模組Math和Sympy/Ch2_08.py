#Sympy模組-可以用來解決線性代數的問題
from sympy import *
x = Symbol('x')
print(x + x + 2)
print(x.name) #印出用symbol定義的名稱

#可以用symbols簡化程式
'''a = symbols('a')
b = symbols('b')
c = symbols('c')'''
a,b,c = symbols('a b c')
print(a.name)
print(b.name)
print(c.name)

y = symbols('y')
z = 5 * x + 6 * y+ x * y
print(z)