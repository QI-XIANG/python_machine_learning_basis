import matplotlib.pyplot as plt
import math

n = 10
success = 0.35
fail = 1 - success
p = []

def probability(k):
    num = (math.factorial(n)) / (math.factorial(n-k)*math.factorial(k))
    pro = num * success**k * (1-success)**(n-k)
    return pro

for k in range(0, n+1):
    if(k == 0):
        p.append(fail**n)
        continue
    if(k == n):
        p.append(success**n)
        continue
    p.append(probability(k))

for i in range(len(p)):
    print("銷售 {} 單位成功機率 {}%".format(i, p[i]*100))

x = [i for i in range(0, n+1)]
width = 0.35
plt.xticks(x)
plt.bar(x, p, width, color='g')
plt.ylabel('Probability')
plt.xlabel('unit:100')
plt.title('Binomial Distribution')
plt.show()