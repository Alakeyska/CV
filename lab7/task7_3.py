# Цель этого задания - научиться использовать функцию HoughCircles().
#
# Для выполнения этого задания нарисуйте 5 окружностей с разным радиусом. Ваша задача - найти каждую окружность
# в отдельности, изменяя параметры функции. В результате у вас должно получиться 5 изображений,
# на каждом из которых выделена только одна окружность. Для упрощения расчетов можно использовать
# радиусы, кратные стороне изображения.
import cv2
import numpy as np

path = "S:\\CV\\lab7\\circles.png"

img = cv2.imread(path, cv2.IMREAD_COLOR)
img_circles = [img.copy(), img.copy(), img.copy(), img.copy(), img.copy()]
each_circle = np.zeros((1, 5, 3), np.int32)

A = img.shape[0]
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_g = cv2.GaussianBlur(img_g, (11, 11), 0)
cv2.imshow('gaus', img_g)

circles_all = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4)
circles_rows = circles_all[0]
circle_0 = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4,
                            maxRadius=int(circles_rows[0][2]), minRadius=int(circles_rows[1][2]) + 1)

if circles_all is not None:
    for circle in circle_0[0]:
        print(circle)
        cv2.circle(img, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)
cv2.imshow('HoughCircles', img)
cv2.waitKey()

# each circle hard way


# # each circle easy way
# i = 0
# for circle in all_circles[0]:
#     circle_name = str(i) + 'circle'
#
#     cv2.circle(img_circles[i], (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)
#     cv2.imshow(circle_name, img_circles[i])
#     cv2.waitKey()
#     i+=1
