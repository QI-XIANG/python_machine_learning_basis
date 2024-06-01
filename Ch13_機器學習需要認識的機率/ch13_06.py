import random
import math
import matplotlib.pyplot as plt

trials = 5000
radius = 50
for i in range(trials):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    if math.sqrt((x-50)**2 + (y-50)**2) < radius:
        plt.scatter(x, y, marker='.', c='y')
    else:
        plt.scatter(x, y, marker='.', c='g')

plt.axis('equal')
plt.show()