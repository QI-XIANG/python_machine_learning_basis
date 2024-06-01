from fractions import Fraction

x = Fraction(2, 7) * Fraction(1, 6)
y = Fraction(5, 7) * Fraction(2, 6)
p = x + y

print("第一位抽籤的中獎機率 {}".format(Fraction(2, 7)))
print("第二位抽籤的中獎機率 {}".format(p))