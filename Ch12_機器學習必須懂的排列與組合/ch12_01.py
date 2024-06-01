import itertools
n = {1, 2, 3, 4}
r = 3
A = set(itertools.permutations(n, r))
print("元素數量 = {}".format(len(A)))
for a in A:
    print(a)