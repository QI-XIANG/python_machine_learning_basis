import numpy as np

a = np.array([4, 2])
b = np.array([1, 3])

ab_cross = np.cross(a, b)
area = np.linalg.norm(ab_cross) / 2

print("area = {0:5.2f}".format(area))