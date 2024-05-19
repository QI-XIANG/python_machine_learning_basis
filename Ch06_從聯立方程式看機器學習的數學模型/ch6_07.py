import matplotlib.pyplot as plt
import numpy as np
from sympy import solve, Symbol

x = Symbol('x')
y = Symbol('y')
eq1 = x - y
eq2 = - x - y + 2
ans = solve((eq1, eq2))
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))

line1_x = np.linspace(-5, 5 , 10)
line1_y = [y for y in line1_x]
line2_x = np.linspace(-5, 5, 10)
line2_y = [- y + 2 for y in line2_x]

plt.plot(line1_x, line1_y)
plt.plot(line2_x, line2_y)

plt.plot(ans[x], ans[y], '-o')
plt.text(ans[x] - 0.5, ans[y] + 0.3, '(' + str(ans[x]) + ',' + str(ans[y]) + ')')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axis('equal')
plt.grid()
plt.show()
