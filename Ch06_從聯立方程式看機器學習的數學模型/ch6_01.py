from sympy import Symbol, solve

a = Symbol('a')
b = Symbol('b')
eq1 = a + b - 1
eq2 = 5 * a + b - 2
ans = solve((eq1, eq2))
print(type(ans))
print(ans)
print("a = {}".format(ans[a]))
print("b = {}".format(ans[b]))