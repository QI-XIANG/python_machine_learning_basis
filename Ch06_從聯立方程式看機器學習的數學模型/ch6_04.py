import matplotlib.pyplot as plt
import numpy as np

a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_y = 48
pt_x = (pt_y + 18) / 0.03
print('獲利48萬需要有 {} 來客數'.format(int(pt_x)))
plt.plot(x, y)
plt.plot(pt_x, pt_y, '-o', color='r')
plt.text(pt_x - 200, pt_y + 5, '(' + str(int(pt_x)) + ',' + str(int(pt_y)) + ')')
plt.xlabel('Customers')
plt.ylabel('Profit')
plt.grid()
plt.show()