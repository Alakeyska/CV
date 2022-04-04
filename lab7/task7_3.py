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


circles_all = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4)
circles_rows = circles_all[0]



circle_0 = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4,
                            maxRadius=int(circles_rows[0][2]) + 1, minRadius=int(circles_rows[1][2]) + 1)
circle_1 = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4,
                            maxRadius=int(circles_rows[1][2]) + 1, minRadius=int(circles_rows[2][2]) + 1)
circle_2 = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4,
                            maxRadius=int(circles_rows[2][2]) + 1, minRadius=int(circles_rows[3][2]) + 1)
circle_3 = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4,
                            maxRadius=int(circles_rows[3][2]) + 1, minRadius=int(circles_rows[4][2]) + 1)
circle_4 = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4,
                            maxRadius=int(circles_rows[4][2]) + 1, minRadius=int(circles_rows[4][2]) - 1)

each_circle = [circle_0, circle_1, circle_2, circle_3, circle_4]
i = 0
if each_circle is not None:
    for HoughCircles in each_circle:
        for circle in HoughCircles[0]:
            print(circle)
            circle_name = str(i) + 'circle'
            cv2.circle(img_circles[i], (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)
            cv2.imshow(circle_name, img_circles[i])
            cv2.waitKey()
        i+=1
        # cv2.circle(img, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)

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
