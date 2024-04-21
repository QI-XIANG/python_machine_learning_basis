#將剛剛儲存的圖檔讀取出來
import matplotlib.pyplot as plt
import matplotlib.image as img

fig = img.imread('out1_14.jpg') #和opencv很像
plt.imshow(fig)
plt.show()