import numpy as np

n = np.linspace(1.1, 10, 90)
count = 0
for i in n:
    count += 1
    print("{0:2.1f} = {1:4.3f}".format(i, np.log10(i)), end="  ")
    if count % 5 == 0:
        print()