import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve

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

x = np.linspace(0, 5, 50)
y = [(ans[a]*y**2 + ans[b]*y + ans[c]) for y in x]
plt.plot(x, y)

x4 = 4
y4 = ans[a]*x4**2 + ans[b]*x4 + ans[c]
plt.plot(x4, y4, '-o')
plt.text(x4-0.7, y4-50, '('+str(x4)+', '+str(y4)+')')

plt.plot(1, 500, '-x', color='b')
plt.text(1-0.7, 500-50, '(1, 500)')

plt.plot(2, 1000, '-x', color='b')
plt.text(2-0.7, 1000-50, '(2, 1000)')

plt.plot(3, 2000, '-x', color='b')
plt.text(3-0.7, 2000-50, '(3, 2000)')

plt.xlabel("Times(unit=100)")
plt.ylabel("Revenue")
plt.grid()
plt.show()