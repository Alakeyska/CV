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

img1 = cv2.imread(path1, cv2.IMREAD_REDUCED_COLOR_2)
img2 = cv2.imread(path2, cv2.IMREAD_REDUCED_COLOR_2)
img1_reduced = cv2.imread(path1, cv2.IMREAD_REDUCED_COLOR_4)
img2_reduced = cv2.imread(path2, cv2.IMREAD_REDUCED_COLOR_4)

# BILATERAL
img1_bilateral = cv2.bilateralFilter(img1, d=60, sigmaColor=50, sigmaSpace=60)
img2_bilateral = cv2.bilateralFilter(img2, d=70, sigmaColor=50, sigmaSpace=70)
img1_reduced_bilateral = cv2.bilateralFilter(img1_reduced, d=60, sigmaColor=50, sigmaSpace=60)
img2_reduced_bilateral = cv2.bilateralFilter(img2_reduced, d=70, sigmaColor=50, sigmaSpace=70)

color_noise_images = {'Original Image': img1, 'Bilateral': img1_bilateral, 'Bilateral_reduced': img1_reduced_bilateral}
mono_noise_images = {'Original Image': img2,'Bilateral': img2_bilateral, 'Bilateral_reduced': img2_reduced_bilateral}

fig1 = plt.figure('Color noise', figsize=(10, 7))
for title, image in color_noise_images.items():
    fig1.add_subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    i += 1
i = 0

fig2 = plt.figure('Mono noise', figsize=(10, 7))
for title, image in mono_noise_images.items():
    fig2.add_subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    i += 1
plt.show()



# for x in range(40):
#     new_ksize = 2 * x + 1
#     c = x*10
#     window_name = 'img1_gauss' + str(new_ksize)
#     ksize = [new_ksize, new_ksize]
#     img1_gauss = cv2.blur(img1, ksize)
#     cv2.imshow(window_name, img1_gauss)
#     if cv2.waitKey() == ord('q'):
#         break
#     cv2.destroyWindow(window_name)
