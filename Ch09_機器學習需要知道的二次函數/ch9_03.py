from sympy import Symbol, solve

x = Symbol('x')
f = Symbol('f')
f = 3*(x-2)**2 - 2
root = solve(f)
print(root)