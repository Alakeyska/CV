import cv2

path = 'S:\\CV\\lab1\\image.jpg'
window_name = 'window1'

if __name__ == '__main__':
    img = cv2.imread(path, flags=cv2.IMREAD_COLOR)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(500)

    img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(700)

    img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_COLOR_2)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(900)
    #
    img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_4)
    cv2.imshow(window_name, img)
    key = cv2.waitKey(1100)