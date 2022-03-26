import cv2


def what_is_figure(contours, img):
    i = 0
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        arcL = cv2.arcLength(contours[i], True)
        s = cv2.contourArea(contours[i])
        if w == h:
            is_square = (arcL ** 2) / (4 * s) == 4
            if is_square:
                cv2.rectangle(img, (x, y), (x + w, y + h), square_color, 2)
                cv2.putText(img, 'square', (x, y), font, fontScale, square_color, text_thickness)
            else:
                cv2.drawContours(img, [contours[i]], 0, circle_color, 2)
                cv2.putText(img, 'circle', (x, y), font, fontScale, circle_color, text_thickness)
        else:
            print(w,h)
            perimeter = (w + h) * 2 - 4
            if perimeter == arcL:
                cv2.rectangle(img, (x, y), (x + w, y + h), rectangle_color, 2)
                cv2.putText(img, 'rectangle', (x, y), font, fontScale, rectangle_color, text_thickness)
        i += 1
    return img


path = 'S:\\CV\\lab6\\6.png'

square_color = (0, 238, 253)
circle_color = (0, 0, 255)
rectangle_color = (255, 0, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
text_thickness = 2

img = cv2.imread(path, cv2.IMREAD_COLOR)
cv2.imshow('original', img)

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_t = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(img_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
new_image = img
cv2.imshow('new', what_is_figure(contours, new_image))
cv2.waitKey()
