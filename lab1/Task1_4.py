import cv2
from datetime import date

black_color = (0, 0, 0)
cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    today = date.today()
    d2 = today.strftime("%d/%m/%Y")
    cv2.putText(gray, d2, (400, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, black_color, 2)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
