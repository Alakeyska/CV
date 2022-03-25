# Протестировать работу детектора границ Кенни на изображениях с четкими и нечеткими границами.
# Пример изображения с четкими границами:

# Пример изображения с нечеткими границами (здесь представим, что финальная задача - выделить полосы разметки.
# На этапе выделения границ достаточно выделить границы вокруг полос и границы вокруг других частей изображения,
# которые позже будут отфильтрованы другими методами)
import cv2
from task5_1 import print_images
from matplotlib import pyplot as plt

path_clear = "S:\\CV\\lab3\\3-1.PNG"
path_parking = "S:\\CV\\lab5\\parking.jpg"

img_clear = cv2.imread(path_clear, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img_clear_blur = cv2.GaussianBlur(img_clear, (13, 13), 0)
canny_clear_blur = cv2.Canny(img_clear_blur, threshold1=20, threshold2=60, apertureSize=3)
clear = {'original': img_clear, 'GaussianBlur': img_clear_blur, 'Canny': canny_clear_blur}

img_parking = cv2.imread(path_parking, cv2.IMREAD_REDUCED_GRAYSCALE_2)
img_parking_blur = cv2.GaussianBlur(img_parking, (13, 13), 0)
canny_parking_blur = cv2.Canny(img_parking_blur, threshold1=25, threshold2=50, apertureSize=3)
parking = {'original': img_parking, 'GaussianBlur': img_parking_blur, 'Canny': canny_parking_blur}

fig1 = plt.figure('Clear borders', figsize=(10, 7))
print_images(clear, fig1, 3, 1)
fig2 = plt.figure('Parking', figsize=(10, 7))
print_images(parking, fig2, 3, 1)
plt.show()

# debug
# for x in range(20):
#     t1 = x * 5
#     t2 = t1 * 2
#     win_name = 't1 = ' + str(t1) + ' t2 = ' + str(t2)
#     canny_parking_blur = cv2.Canny(img_parking_blur, threshold1=t1, threshold2=t2, apertureSize=3)
#     cv2.imshow(win_name, canny_parking_blur)
#     if cv2.waitKey() == ord('q'):
#         break
#     cv2.destroyWindow(win_name)
