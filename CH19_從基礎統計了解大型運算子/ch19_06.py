x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

#計算變異數
var = 0
for v in x:
    var += (v - mean) ** 2
var /= len(x)
sd = var ** 0.5
print("標準差 = {0:6.2f}".format(sd))