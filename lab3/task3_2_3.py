# Для выполнения этого задания используйте изображения 3-3 и 3-4 (угадайте, где их взять). Целью этогозадания является
# очистка изображения от шума. Используя полученные навыки, определите какие фильтры для этого подходят наилучшим
# образом. Исследуйте изображения как с цветным, так и с монохромным шумом. Отличаются ли результаты при изменении
# разрешения картинки? Попробуйте применить фильтры как к цветному изображению, так и к изображению в оттенках серого.

import cv2
import numpy as np
from matplotlib import pyplot as plt

path1 = "S:\\CV\\lab3\\3-3.PNG"
path2 = "S:\\CV\\lab3\\3-4.PNG"
i = 0

img1 = cv2.imread(path1, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img2 = cv2.imread(path2, cv2.IMREAD_REDUCED_GRAYSCALE_2)

# GAUS
img1_gauss = cv2.GaussianBlur(img1, (11, 11), 0)
img2_gauss = cv2.GaussianBlur(img2, (13, 13), 0)

# BILATERAL
img1_bilateral = cv2.bilateralFilter(img1, d=60, sigmaColor=35, sigmaSpace=60)
img2_bilateral = cv2.bilateralFilter(img2, d=70, sigmaColor=35, sigmaSpace=70)

color_noise_images = {'Original Image': img1, 'Gaus': img1_gauss, 'Bilateral': img1_bilateral}
mono_noise_images = {'Original Image': img2, 'Gaus': img2_gauss, 'Bilateral': img2_bilateral}

fig1 = plt.figure('Color noise', figsize=(10, 7))
for title, image in color_noise_images.items():
    fig1.add_subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 'gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    i += 1
i = 0

fig2 = plt.figure('Mono noise', figsize=(10, 7))
for title, image in mono_noise_images.items():
    fig2.add_subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 'gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    i += 1
plt.show()

# debug
# cv2.imshow('orig img2', img2)
# for x in range(40):
#     new_ksize = 2 * x + 1
#     c = x*10
#     window_name = 'img2_bilateral, sigmaColor is ' + str(c)
#     ksize = [new_ksize, new_ksize]
#     img1_bilateral = cv2.bilateralFilter(img2, d=60, sigmaColor=c, sigmaSpace=60)
#     cv2.imshow(window_name, img1_bilateral)
#     if cv2.waitKey() == ord('q'):
#         break
#     cv2.destroyWindow(window_name)
