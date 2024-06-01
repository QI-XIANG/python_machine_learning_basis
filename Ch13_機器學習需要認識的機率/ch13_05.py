import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1 
    y = random.random() * 2 - 1
    if x * x + y * y <= 1:
        Hits += 1

PI = 4 * Hits / trials

print("PI = {}".format(PI))