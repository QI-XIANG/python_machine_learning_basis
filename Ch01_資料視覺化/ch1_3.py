import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares) 
plt.axis([0, 8, 0, 70]) #x軸刻度0~8，y軸刻度0~70
plt.show()