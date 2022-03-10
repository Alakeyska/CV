# Для выполнения этого задания используйте результат, который вы получили при выполнении второго задания во второй
# лабораторной. Там у вас получилась картинка с шумом: точки на фоне или разрывы на границах. Пример картинки:
# Примените морфологические преобразования к такому изображению так, чтобы максимально убрать шум в виде точек на фоне
# и при этом закрыть разрывы в линиях текста

import cv2
import numpy as np
from matplotlib import pyplot as plt

path_text = "S:\\CV\\lab4\\4-1.png"
path = 'S:\\CV\\lab4\\emoji.jpg'
i = 0

img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_4)
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 89,9)

kernel = np.ones((3, 3), np.uint8)
img_erode = cv2.erode(adaptive, kernel, iterations=1)
img_dilate = cv2.dilate(img_erode, kernel, iterations=2)
images = {'Original': adaptive, 'Step 1 - erode': img_erode, 'Step 2 - dilate': img_dilate}

fig = plt.figure('Morphology', figsize=(10, 7))
for title, image in images.items():
    fig.add_subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 'gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis('off')
    i += 1
plt.show()


# img_text = cv2.imread(path_text, flags=cv2.IMREAD_GRAYSCALE)
# ret, thresh = cv2.threshold(img_text, 127, 255, cv2.THRESH_BINARY_INV)
#
# text_erode = cv2.erode(thresh,kernel,iterations=1)
# text_dilate = cv2.dilate(text_erode, kernel, iterations=3)
# cv2.imshow('dilate', text_dilate)
# cv2.waitKey()

# for i in range(15):
#
#     cv2.imshow('morph iteration is' + str(i), img_morph)
#     if cv2.waitKey() == ord('q'):
#         break

