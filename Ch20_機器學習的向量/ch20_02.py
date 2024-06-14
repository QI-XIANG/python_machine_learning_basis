import numpy as np
import math

a = np.array([1, 1])
b = np.array([5, 5])
c = np.array([1, 5])
d = np.array([5, 1])

ab = b - a
cd = d - c

norm_a = np.linalg.norm(ab)
norm_b = np.linalg.norm(cd)

dot_ab = np.dot(ab, cd)

cos_angle = dot_ab / (norm_a * norm_b)
rad = math.acos(cos_angle)
deg = math.degrees(rad)
print("角度是 = {}".format(deg))