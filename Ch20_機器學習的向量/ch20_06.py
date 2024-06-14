import numpy as np
import math

a = np.array([4, 2])
b = np.array([1, 3])

norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

dot_ab = np.dot(a, b)

cos_angle = dot_ab / (norm_a * norm_b)
rad = math.acos(cos_angle)

area = norm_a * norm_b * math.sin(rad) / 2
print("area = {0:5.2f}".format(area))