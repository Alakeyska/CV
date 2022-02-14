import cv2
import numpy as np

new_path = 'S:\\CV\\lab1\\chess.png'
window_name = 'window1'
image_width, image_length = 500, 750
is_magenta = True
square_size = (image_width + image_length) / 10
img_chess = np.full((image_length, image_width, 3), (255, 255, 255), 'uint8')
magenta_color = np.full(3, (255, 0, 255), 'uint8')

if __name__ == '__main__':
    for x in range(image_length):
        if x % square_size == 0:
            is_magenta = not is_magenta
        for y in range(image_width):
            if y % square_size == 0:
                is_magenta = not is_magenta
            if is_magenta:
                img_chess[x][y] = magenta_color
    cv2.imshow(window_name, img_chess)
    res = cv2.imwrite(new_path, img_chess)
    key = cv2.waitKey(0)
