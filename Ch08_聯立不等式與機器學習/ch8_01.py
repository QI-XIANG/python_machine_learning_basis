import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

x = Symbol('x')
y = Symbol('y')
eq1 = 8 - 0.6 * x - y
eq2 = 17.5 - 2.5 * x - y
ans = solve((eq1,eq2))
print('x = {}'.format(int(ans[x])))
print('y = {}'.format(int(ans[y])))

z = 50 * int(ans[x]) + 50 * int(ans[y])
print('最大獲利 = {}萬'.format(z))

