import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

plt.plot([0, 0], [20, 0])
plt.plot([0, 0], [0, 20])

line3_x = np.linspace(0, 20, 20)
line3_y = [(8 - 0.6 * y) for y in line3_x]

line4_x = np.linspace(0, 20, 20)
line4_y = [(17.5 - 2.5 * y) for y in line4_x]

lineObj_x = np.linspace(0, 20, 20)
lineObj_y = [(10 - y) for y in lineObj_x]

plt.axis([0, 20, 0, 20])

plt.plot(line3_x, line3_y)
plt.plot(line4_x, line4_y)
plt.plot(lineObj_x, lineObj_y)

plt.plot(5, 5, '-o')
plt.text(4.5, 5.5, '(5, 5)')
plt.xlabel('Research')
plt.ylabel('UI')
plt.grid()
plt.show()