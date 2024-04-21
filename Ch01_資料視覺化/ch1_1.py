import matplotlib.pyplot as plt

x = [x for x in range(9)] #產生0~8串列
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(x, squares) #squares是y軸上的值
plt.show()