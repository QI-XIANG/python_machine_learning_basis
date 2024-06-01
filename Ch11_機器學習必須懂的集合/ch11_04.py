math = {'Kevin', 'Peter', 'Eric'}
physics = {'Peter', 'Nelson', 'Tom'}
allmember1 = math | physics
print("參加數學或物理夏令營的成員 ", allmember1)
allmember2 = math.union(physics)
print("參加數學或物理夏令營的成員 ", allmember2)