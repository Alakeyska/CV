import cv2
import numpy as np

print(cv2.__version__)
# path='D:\\8491\\Salam\\lab1\\test_img.png'
# new_path='D:\\8491\\Salam\\lab1\\new_img.png'
# window_name='window1'

# img=cv2.imread(path, flags=cv2.IMREAD_COLOR)
# res = cv2.imwrite(new_path, img)

# cv2.namedWindow(window_name,flags=cv2.WINDOW_AUTOSIZE)
# cv2.imshow(window_name, img)
# key = cv2.waitKey(0)


path = 'S:\\CV\\lab1\\image.jpg'
window_name = 'window1'
blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)
black_color = (0, 0, 0)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
text_thickness = 2

# Task1
# img = cv2.imread(path, flags=cv2.IMREAD_COLOR)
# cv2.imshow(window_name, img)
# key = cv2.waitKey(500)
#
# img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
# cv2.imshow(window_name, img)
# key = cv2.waitKey(700)
#
# img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_COLOR_2)
# cv2.imshow(window_name, img)
# key = cv2.waitKey(900)
# #
# img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_4)
# cv2.imshow(window_name, img)
# key = cv2.waitKey(1100)

# Task2
img_white = np.full((480, 640, 3), (255, 255, 255), 'uint8')
cv2.circle(img_white, (500, 100), 50, blue_color, 3)
cv2.putText(img_white, 'circle', (350, 100), font, fontScale, black_color, text_thickness)

cv2.rectangle(img_white, (10, 350), (200, 450), red_color, 3)
cv2.putText(img_white, 'rectangle', (40, 325), font, fontScale, black_color, text_thickness)

cv2.line(img_white, (0, 0), (640, 480), green_color, 3)
cv2.putText(img_white, 'line', (300, 200), font, fontScale, black_color, text_thickness)
cv2.imshow(window_name, img_white)

key = cv2.waitKey(0)

# if __name__ == '__main__':
