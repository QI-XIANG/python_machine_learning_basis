math = {'Kevin', 'Peter', 'Eric'}
physics = {'Peter', 'Nelson', 'Tom'}
math_only1 = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ", math_only1)
math_only2 = math.difference(physics)
print("參加數學夏令營同時沒有參加物理夏令營的成員 ", math_only2)
physics_only1 = physics - math
print("參加物理夏令營同時沒有參加數學夏令營的成員 ", physics_only1)
physics_only2 = physics.difference(math)
print("參加物理夏令營同時沒有參加數學夏令營的成員 ", physics_only2)