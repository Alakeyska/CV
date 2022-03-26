# Вам нужно смоделировать видеоряд с камеры, которая установлена на мобильном роботе. Робот снимает дорогу под
# некоторым углом, камера смотрит вперед. Задача робота - остановиться перед линией разметки. Возьмите лист бумаги,
# маркер (или принтер) и смоделируйте такую разметку. Запишите видео, которое бы получал робот с такой камеры.
# На полученном видео выделите границы так, чтобы на следующих шагах можно было найти линию.

import numpy as np
import cv2

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
    cv2.imshow('canny', canny)
    cv2.imshow('gray', gray)
    if cv2.waitKey(25) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# path_line = "S:\\CV\\lab5\\garbage_line.png"
# line=cv2.imread(path_line,cv2.IMREAD_REDUCED_GRAYSCALE_2)
# blur = cv2.GaussianBlur(line, (15, 15), 0)
# # canny = cv2.Canny(blur, 20, 40, apertureSize=3)
# # cv2.imshow('frame', canny)
# # cv2.waitKey()
#
# # debug
# for x in range(20,100):
#     t1 = x * 5
#     t2 = t1 * 2
#     win_name = 't1 = ' + str(t1) + ' t2 = ' + str(t2)
#     canny_parking_blur = cv2.Canny(blur, threshold1=t1, threshold2=t2, apertureSize=3)
#     cv2.imshow(win_name, canny_parking_blur)
#     if cv2.waitKey() == ord('q'):
#         break
#     cv2.destroyWindow(win_name)

# 90,180,110,220
