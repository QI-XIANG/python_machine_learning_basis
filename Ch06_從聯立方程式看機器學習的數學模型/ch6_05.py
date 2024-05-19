import matplotlib.pyplot as plt
import numpy as np
from sympy import solve, Symbol

x = Symbol('x')
y = Symbol('y')
eq1 = x + y - 35
eq2 = 2 * x + 4 * y - 100
ans = solve((eq1,eq2))
print('雞 = {}'.format(ans[x]))
print('兔 = {}'.format(ans[y]))

line1_x = np.linspace(0, 100, 100)
line1_y = [35 - y for y in line1_x]
line2_x = np.linspace(0, 100, 100)
line2_y = [25 - 0.5 * y for y in line2_x]

plt.plot(line1_x, line1_y)
plt.plot(line2_x, line2_y)

plt.plot(ans[x], ans[y], '-o', color='r')
plt.text(ans[x] - 5, ans[y] + 5, '(' + str(ans[x]) + ',' + str(ans[y]) + ')')
plt.xlabel('Chicken')
plt.ylabel('Rabbit')
plt.grid()
plt.show()