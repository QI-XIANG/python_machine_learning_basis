math = {'Kevin', 'Peter', 'Eric'}
physics = {'Peter', 'Nelson', 'Tom'}
math_sydi_physics1 = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ", math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("沒有同時參加數學和物理夏令營的成員 ", math_sydi_physics2)