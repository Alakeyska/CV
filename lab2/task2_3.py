import cv2

path = 'S:\\CV\\lab2\\lab2-4.mp4'
out_path = 'S:\\CV\\lab2\\out.mp4'

cap = cv2.VideoCapture(path)
# # Video REC
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(out_path, -1, 30.0, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret_otsu, thresh = cv2.threshold(gray, 111, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # out.write(thresh)
        cv2.imshow('frame', thresh)
        print(ret_otsu)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
# out.release()
