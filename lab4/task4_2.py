# Для выполнения этого задания используйте результат, который вы получили при выполнении третьего задания второй
# лабораторной. Если вы не выполняли это задание, возьмите результат у коллеги.
# К полученному видео примените морфологические преобразования так, чтобы убрать шум с фона и разрывы в разметке

import cv2
import numpy as np

path = 'S:\\CV\\lab2\\lab2-4.mp4'
out_path = 'S:\\CV\\lab2\\out.mp4'

cap = cv2.VideoCapture(path)
# # Video REC
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# out = cv2.VideoWriter(out_path, -1, 30.0, (frame_width, frame_height))
kernel = np.ones((3, 3), np.uint8)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret_otsu, thresh = cv2.threshold(gray, 111, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # out.write(thresh)
        thresh_morph = cv2.erode(thresh, kernel, iterations=3)
        thresh_morph = cv2.dilate(thresh_morph, kernel, iterations=8)
        cv2.imshow('frame', thresh_morph)
        cv2.imshow('original', thresh)
        # print(ret_otsu)
        if cv2.waitKey(0) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
