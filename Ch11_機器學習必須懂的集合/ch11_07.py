from sympy import *
A = FiniteSet('a', 'b')
B = FiniteSet('c', 'd')
AB = A*B
for ab in AB:
    print(type(ab), ab)