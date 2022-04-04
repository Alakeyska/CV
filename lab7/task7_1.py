# Цель выполнения этого задания - научиться использовать функции HoughLines() и HoughLinesP() на простых примерах
#
# Для выполнения этого задания создайте изображение с отрезками разной длины и под разными углами. Ваша задача:
# найти все прямые, на которых лежат отрезки, с помощью функции HoughLines()
# найти все прямые, на которых лежат только горизонтальные и вертикальные отрезки, с помощью функции HoughLines()
# Найти самый длинный и самый короткий отрезок с помощью функции HoughLinesP

import cv2
import math
import numpy as np


# рисование линий HoughLines
def draw_line(rho, theta, img, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = cos_t * rho
    y0 = sin_t * rho
    pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t)
    pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t)
    cv2.line(img, pt1, pt2, color, thickness, lineType)


# рисование линий HoughLinesP
def draw_line_P(x0, y0, x1, y1, img, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA):
    cv2.line(img, (x0, y0), (x1, y1), color, thickness, lineType)


def deg_to_rad(deg):
    return deg * math.pi / 180


path = 'S:\\CV\\lab7\\lines.png'
img = cv2.imread(path, cv2.IMREAD_COLOR)
img_HV = img
img_SL = img
img_g = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('orig', img)

# lines = cv2.HoughLines(img_g, 1, deg_to_rad(0.5), 275)
#
# for line in lines:
#     print('line:', line)
#     line = line[0]
#     draw_line(line[0], line[1], img)
#
# cv2.imshow('LINES', img)
# cv2.waitKey()

# # only vertical and horiz
# lines_V_H = cv2.HoughLines(img_g, 1, deg_to_rad(10), 75)
# for line in lines_V_H:
#     print('line:', line)
#     line = line[0]
#     draw_line(line[0], line[1], img_HV)
# cv2.imshow('HORIZONTAL AND VERTICAL ONLY',img_HV)
# cv2.waitKey()

# shortest and longest

# # longest - 360
# lines_S_L = cv2.HoughLinesP(img_g, 1, deg_to_rad(0.5),290, minLineLength=360)
# print(lines_S_L)
# print("lines:", len(lines_S_L))
#
# for [[x0, y0, x1, y1]] in lines_S_L:
#     draw_line_P(x0, y0, x1, y1, img, thickness=2)
# cv2.imshow('SHORT AND LONG', img_HV)
# cv2.waitKey()


lines_P = cv2.HoughLinesP(img_g, 1, deg_to_rad(0.5), 290, minLineLength=200)
lines_S_H_len = [1000, 0]
lines_S_H = np.zeros((2, 1, 4), np.int32)

# print(lines_P)
# print("lines:", len(lines_P))

# finding longest and shortest
for [[x0, y0, x1, y1]] in lines_P:
    lengh_line = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    if lengh_line > lines_S_H_len[1]:
        lines_S_H_len[1] = lengh_line
        lines_S_H[1] = [[x0, y0, x1, y1]]
    if lengh_line < lines_S_H_len[0]:
        lines_S_H_len[0] = lengh_line
        lines_S_H[0] = [[x0, y0, x1, y1]]
    print('lengh is', lengh_line)
    # draw_line_P(x0, y0, x1, y1, img, thickness=2)

for [[x0, y0, x1, y1]] in lines_S_H:
    draw_line_P(x0, y0, x1, y1, img, thickness=2)
# print(lines_S_H_len)
# print(lines_S_H)
cv2.imshow('SHORT AND LONG', img_HV)
cv2.waitKey()
