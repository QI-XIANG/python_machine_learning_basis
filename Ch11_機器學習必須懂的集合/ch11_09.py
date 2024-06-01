from sympy import *
A = FiniteSet('a', 'b')
AAA = A**3
print('The length of Cartesian product', len(AAA))
for a in AAA:
    print(a)