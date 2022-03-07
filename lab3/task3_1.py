# Для выполнения этого задания используйте изображения 3-1 и 3-2 (они лежат на диске). Примените к ним все известные
# фильтры для сглаживания изображений. Определите, какие из них больше всего подходят для того, чтобы максимально
# убрать все неровности на изображениях. Попробуйте применить фильтры как к цветному изображению,
# так и к изображению в оттенках серого.

import cv2
import numpy as np
from matplotlib import pyplot as plt

path1 = "S:\\CV\\lab3\\3-1.PNG"
path2 = "S:\\CV\\lab3\\3-2.PNG"
img1 = cv2.imread(path1, cv2.IMREAD_REDUCED_COLOR_2)
img2 = cv2.imread(path2, cv2.IMREAD_REDUCED_COLOR_2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

# BLUR
# img1_blur = cv2.blur(img1, (15, 15))
# cv2.imshow('img1_BLUR', img1_blur)
#
# img2_blur = cv2.blur(img2, (13, 13))
# cv2.imshow('img2_BLUR', img2_blur)
# cv2.waitKey()


# BOX FILTER
# img1_box = cv2.boxFilter(img1, -1, (15, 15))
# cv2.imshow('img1_box', img1_box)
#
# img2_box = cv2.boxFilter(img2, -1, (13, 13))
# cv2.imshow('img2_box', img2_box)
# cv2.waitKey()


# MEDIAN FILTER
# img1_median = cv2.medianBlur(img1, 11)
# cv2.imshow('img1_median', img1_median)
#
# img2_median = cv2.medianBlur(img2, 11)
# cv2.imshow('img2_median', img2_median)
# cv2.waitKey()

# GAUSSIAN
# img1_gaussian = cv2.GaussianBlur(img1, (17, 17), 0)
# cv2.imshow('img1_gaussian', img1_gaussian)
#
# img2_gaussian = cv2.GaussianBlur(img2, (21,21), 0)
# cv2.imshow('img2_gaussian', img2_gaussian)
# cv2.waitKey()

# BILATERAL
img1_bilateral = cv2.bilateralFilter(img1, d=-1, sigmaColor=90, sigmaSpace=20)
cv2.imshow('img1_bilateral', img1_bilateral)

img2_bilateral = cv2.bilateralFilter(img2, d=40, sigmaColor=200, sigmaSpace=40)
cv2.imshow('img2_bilateral', img2_bilateral)
cv2.waitKey()

# debug

# for x in range(40):
#     c = x * 10
#     new_ksize = 2 * x + 1
#     window_name = 'img2_gauss' + str(c)
#     ksize = [new_ksize, new_ksize]
#
#     # img1_bilateral = cv2.bilateralFilter(img1, d=13, sigmaColor=60, sigmaSpace=13)
#     img2_bilateral = cv2.bilateralFilter(img2, d=40, sigmaColor=200, sigmaSpace=40)
#
#     # cv2.imshow('s = 13', img1_bilateral)
#     cv2.imshow(window_name, img2_bilateral)
#     if cv2.waitKey() == ord('q'):
#         break
#     cv2.destroyWindow(window_name)



