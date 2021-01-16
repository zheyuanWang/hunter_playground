from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('test.jpg')
r, g ,b= img.split()
data = np.array(r)
k = np.array([
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
])

def convolution(k, data):
    n, m = data.shape
    kn, km = k.shape
    img_new = np.zeros([n-kn+1,m-km+1])
    for i in range(n - kn + 1):
        for j in range(m - km + 1):
            a = data[i:i + kn, j:j + km]  # 矩阵切片
            img_new[i][j] = np.sum(np.multiply(k, a))
    return np.array(img_new)

img_new = convolution(k, data)


plt.figure("Image")
plt.imshow(img_new,cmap='gray')
plt.show()


#out = Image.fromarray(img_new, 'L')
#out.show()

