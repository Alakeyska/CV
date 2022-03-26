import cv2

path = 'S:\\CV\\lab6\\6.png'
i = 0
img = cv2.imread(path, cv2.IMREAD_COLOR)
cv2.imshow('img_orig', img)
square_color = (0, 238, 253)
circle_color = (0, 0, 255)
rectangle_color = (255, 0, 0)

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_t = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('img_t', img_t)

contours, hierarchy = cv2.findContours(img_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# print('contours', contours)
# print('hierarchy', hierarchy[0])

for i in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    arcL = cv2.arcLength(contours[i], True)
    s = cv2.contourArea(contours[i])
    if w == h:
        is_square = (arcL ** 2) / (4 * s) == 4
        if is_square:
            new = cv2.rectangle(img, (x, y), (x + w, y + h), square_color, 2)
        else:
            new = cv2.rectangle(img, (x, y), (x + w, y + h), circle_color, 2)
    else:
        perimeter = (w + h) * 2
        print('width + height = %f \n arcLen is %f'%(perimeter, arcL))
        if perimeter == arcL + 4:
            new = cv2.rectangle(img, (x, y), (x + w, y + h), rectangle_color, 2)
    # if cv2.waitKey() == ord('q'):
    #     break
    i += 1
cv2.imshow(str(i), new)
cv2.waitKey()
