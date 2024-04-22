#色彩映射color mapping
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100) #產生100個元素的串列
y = x
t = x #用來設定color map的串列

plt.scatter(x, y, c=t, cmap="rainbow") #將color設定為串列
plt.show()
