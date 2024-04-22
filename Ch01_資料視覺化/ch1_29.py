#繪製矩形陣列資料
import matplotlib.pyplot as plt
import numpy as np

img = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15]])

plt.imshow(img, cmap="Blues")
plt.colorbar() #顯示顏色標示
plt.show()