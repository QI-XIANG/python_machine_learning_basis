import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

eq1 = a + b + c - 500
eq2 = 4*a + 2*b + c - 1000
eq3 = 9*a + 3*b + c - 2000
ans = solve((eq1, eq2, eq3))

print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))
print('c = {}'.format(ans[c]))