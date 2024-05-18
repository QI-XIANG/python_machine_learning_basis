import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

a = Symbol('a')
b = Symbol('b')
eq1 = a + b - 1
eq2 = 5 * a + b - 2
ans = solve((eq1, eq2))
print("a = {}".format(ans[a]))
print("b = {}".format(ans[b]))

pt_x1 = 600
pt_y1 = ans[a] * pt_x1 + ans[b]
pt_x2 = 1000
pt_y2 = ans[a] * pt_x2 + ans[b]

x = np.linspace(0, 2500, 250)
y = ans[a] * x + ans[b]
plt.plot(x, y)
plt.plot(pt_x1, pt_y1, '-o')
plt.text(pt_x1 + 60, pt_y1 - 10, 'pt1')
plt.plot(pt_x2, pt_y2, '-o')
plt.text(pt_x2 + 60, pt_y2 - 10, 'pt2')
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()
plt.show()


