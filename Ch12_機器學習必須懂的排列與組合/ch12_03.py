import itertools
n = {'A', 'B', 'C', 'D', 'E'}
r = 5
A = set(itertools.permutations(n, r))
print("業務員路徑數 = {}".format(len(A)))
for a in A:
    print(a)