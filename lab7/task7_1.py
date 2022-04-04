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

if __name__=='__main__':
    path = 'S:\\CV\\lab7\\lines.png'
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img_HV = img.copy()
    img_SL = img.copy()
    img_g = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original', img)

    # all lines
    lines = cv2.HoughLines(img_g, 1, math.radians(0.5), 275)
    print('FIND ALL LINES \nnumber of lines is %d' % len(lines))
    for line in lines:
        print('line:', line)
        line = line[0]
        draw_line(line[0], line[1], img)
    cv2.imshow('LINES', img)
    cv2.waitKey()

    # only vertical and horiz
    lines_V_H = cv2.HoughLines(img_g, 1, math.radians(10), 75)
    print('\nFIND VERTICAL AND HORIZONTAL \nnumber of lines is %d' % len(lines_V_H))
    for line in lines_V_H:
        print('line:', line)
        line = line[0]
        draw_line(line[0], line[1], img_HV)
    cv2.imshow('HORIZONTAL AND VERTICAL ONLY', img_HV)
    cv2.waitKey()

    # shortest and longest
    lines_P = cv2.HoughLinesP(img_g, 1, math.radians(0.5), 290, minLineLength=200)
    print('\nFIND SHORTEST AND LONGEST \nnumber of lines is %d' % len(lines_P))
    lines_S_L_len = [1000, 0]
    lines_S_L = np.zeros((2, 1, 4), np.int32)

    # finding shortest amd longest
    for [[x0, y0, x1, y1]] in lines_P:
        length_line = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        if length_line <= lines_S_L_len[0]:
            lines_S_L_len[0] = length_line
            lines_S_L[0] = [[x0, y0, x1, y1]]
        if length_line > lines_S_L_len[1]:
            lines_S_L_len[1] = length_line
            lines_S_L[1] = [[x0, y0, x1, y1]]
        print('length is', length_line)

    for [[x0, y0, x1, y1]] in lines_S_L:
        draw_line_P(x0, y0, x1, y1, img_SL, thickness=2)
    print('\nshort line length is %f\nlongest line length is %f'%(lines_S_L_len[0], lines_S_L_len[1]))
    cv2.imshow('SHORT AND LONG', img_SL)
    cv2.waitKey()
