# Цель этого задания - научиться использовать функции поиска линий на практике.
#
# Для выполнения этого задания возьмите видео из задания 3 к лабораторной 5 (если вы не выполняли это задание,
# возьмите видео у однокурсников). Ваша задача - найти линию на этом видео с помощью преобразования Хафа.
# Можно найти несколько линий, которые проходят по границам полосы разметки.

import cv2
import math
from task7_1 import draw_line_P

path = "S:\\CV\\lab5\\road.mp4"
path_garbage = "S:\\CV\\lab5\\garbage_road.mp4"
cap = cv2.VideoCapture(path_garbage)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv2.resize(frame, (1024, 576))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15, 15), 0)
    canny = cv2.Canny(blur, 110, 220, apertureSize=3)
    lines = cv2.HoughLinesP(canny, 1, math.radians(1), 120, minLineLength=200, maxLineGap=160)

    if lines is not None:
        for [[x0, y0, x1, y1]] in lines:
            draw_line_P(x0, y0, x1, y1, frame, thickness=2)
    cv2.imshow("LINES", frame)
    cv2.imshow('canny', canny)
    if cv2.waitKey(25) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

