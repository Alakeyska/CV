# Для выполнения этого задания вам понадобится изображение task.png (рисунок 1). В левом верхнем углу изображения нарисована
# зеленая звездочка, которая обведена в прямоугольник. Это шаблон. Задача: среди всех фигур с помощью сравнения моментов
# контуров найти звездочки того же размера, которые повернуты относительно шаблона. Результат поиска представьте в виде изображения,
# на котором все подходящие фигуры выделены (обведены, выделены цветом и т.п.) Объясните, как именно вы решили задачу.
# Аргументируйте решение. На рисунке 2 (answer.png) вы можете увидеть, какие фигуры должны быть выделены.

import cv2
import numpy as np

path_pattern = "S:\\CV\\lab8\\pattern.png"
path_img = "S:\\CV\\lab8\\task.png"

pattern_color = cv2.imread(path_pattern, cv2.IMREAD_COLOR)
pattern = cv2.cvtColor(pattern_color, cv2.COLOR_BGR2GRAY)
pattern = 255 - pattern
pattern = cv2.GaussianBlur(pattern, (3, 3), 0)

img_color = cv2.imread(path_img, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img = 255 - img
img = cv2.GaussianBlur(img, (3, 3), 0)

contours_pattern, _ = cv2.findContours(pattern, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours_img, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

mu_1_0 = cv2.moments(contours_pattern[0])
hu_1_0 = cv2.HuMoments(mu_1_0)
print('mu_pattern: ', mu_1_0)

for i in range(len(contours_img)):
    mu_2_i = cv2.moments(contours_img[i])
    hu_2_i = cv2.HuMoments(mu_2_i)

    if abs((hu_1_0[0] - hu_2_i[0]) / hu_1_0[0]) <= 0.04:
        if abs((mu_1_0['m00'] - mu_2_i['m00']) / mu_1_0['m00']) <= 0.01:
            if not abs((mu_1_0['mu20'] - mu_2_i['mu20']) / mu_1_0['mu20']) <= 0.01:
                print('I found it!')
                cv2.drawContours(img_color, contours_img, i, (255, 0, 255), 2)

cv2.imshow('result', img_color)
cv2.waitKey()
