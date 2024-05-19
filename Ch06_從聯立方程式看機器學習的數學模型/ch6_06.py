import matplotlib.pyplot as plt
import numpy as np
from sympy import solve, Symbol

x = Symbol('x')
y = Symbol('y')
eq1 = x + y - 100
eq2 = 2 * x + 4 * y - 350
ans = solve((eq1,eq2))
print('菜鳥業務員須外出的天數 = {}'.format(ans[x]))
print('資深業務員須外出的天數 = {}'.format(ans[y]))

line1_x = np.linspace(0, 100, 100)
line1_y = [100 - y for y in line1_x]
line2_x = np.linspace(0, 100, 100)
line2_y = [(350 - 2 * y) / 4 for y in line2_x]

plt.plot(line1_x, line1_y)
plt.plot(line2_x, line2_y)

plt.plot(ans[x], ans[y], '-o')
plt.text(ans[x] - 5, ans[y] + 5, '(' + str(ans[x]) + ',' + str(ans[y]) + ')')
plt.xlabel('Junior Salesman')
plt.ylabel('Senior Salesman')
plt.grid()
plt.show()