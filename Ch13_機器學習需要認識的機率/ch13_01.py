import random

min = 1
max = 6
target = 5
n = 10000
counter = 0

for i in range(n):
    if target == random.randint(min, max):
        counter += 1

print("經過 {} 次，得到 {} 次 {}".format(n, counter, target))

p = counter / n

print("機率 P = {}".format(p))