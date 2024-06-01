import matplotlib.pyplot as plt
from random import randint

min = 1
max = 6
times = 10000

dice = [0]*7
for i in range(times):
    data = randint(min, max)
    dice[data] += 1

del dice[0]

for i, c in enumerate(dice, 1):
    print("{} = {} 次".format(i, c))

x = [i for i in range(min, max+1)]
width = 0.35
plt.bar(x, dice, width, color='g')
plt.ylabel('Frequency')
plt.title('Test 10000 times')
plt.show()