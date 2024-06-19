import numpy as np

A = np.matrix([[2,3],[5,7]])
B = np.linalg.inv(A) # 計算 A 的逆矩陣

print("A_inv = {}".format(B))
print("E = {}".format((A * B).astype(np.int64))) # A * A_inv = E