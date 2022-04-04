# Задание 4 (5 баллов из 20)
# Цель этого задания - научиться использовать функцию поиска окружностей на практике.
#
# Для выполнения этого задания возьмите несколько фотографий круглых дорожных знаков.
# Ваша задача - найти знаки на изображении. Перед непосредственно вызовом функции HoughCircles()
# вам может понадобиться дополнительная обработка. Для нее используйте знания, полученные в предыдущих темах.
# Сделайте вывод о том, в каких случаях знаки ищутся неправильно или с погрешностью.
import cv2

path_sign = "S:\\CV\\lab7\\sign.jpg"
path_down = "S:\\CV\\lab7\\sign_down.jpg"
path_two = "S:\\CV\\lab7\\two_sign.jpg"
# READ
sign = cv2.imread(path_sign, cv2.IMREAD_COLOR)
sign_g = cv2.cvtColor(sign, cv2.COLOR_BGR2GRAY)
A = sign_g.shape[0]

sign_down = cv2.imread(path_down, cv2.IMREAD_COLOR)
sign_down_g = cv2.cvtColor(sign_down, cv2.COLOR_BGR2GRAY)
B = sign_down_g.shape[0]

sign_two = cv2.imread(path_two, cv2.IMREAD_COLOR)
sign_two_g = cv2.cvtColor(sign_two, cv2.COLOR_BGR2GRAY)
C = sign_two_g.shape[0]

# first sign
print('One sign task')
sign_g = cv2.GaussianBlur(sign_g, (11, 11), 0)
circles_sign = cv2.HoughCircles(sign_g, cv2.HOUGH_GRADIENT, 1, minDist=A // 16, param1=100, param2=A // 4)

if circles_sign is not None:
    for circle in circles_sign[0]:
        print(circle)
        cv2.circle(sign, (int(circle[0]), int(circle[1])), int(circle[2]), color=(255, 0, 0), thickness=3)

cv2.imshow('find circle', sign)
cv2.waitKey()

# sign down
print('\nOne sign down task')
sign_down_g = cv2.GaussianBlur(sign_down_g, (11, 11), 0)
circles_sign_down = cv2.HoughCircles(sign_down_g, cv2.HOUGH_GRADIENT, 1, minDist=B // 16, param1=100, param2=B // 10) # if param2 = B // 4 - bad result
if circles_sign_down is not None:
    for circle in circles_sign_down[0]:
        print(circle)
        cv2.circle(sign_down, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 0, 255), thickness=3)
    cv2.imshow('Dowm sign', sign_down)
    cv2.waitKey()

# two sign
print('\n Two sign task')
sign_two_g = cv2.GaussianBlur(sign_two_g, (11, 11), 0)
circles_sign_two = cv2.HoughCircles(sign_two_g, cv2.HOUGH_GRADIENT, 1, minDist=C // 5, param1=300, param2=C // 30) # if param 2 = c // 20 - 1 circle
if circles_sign_two is not None:
    for circle in circles_sign_two[0]:
        print(circle)
        cv2.circle(sign_two, (int(circle[0]), int(circle[1])), int(circle[2]), color=(0, 255, 0), thickness=3)
    print('\nnumber of circles is', len(circles_sign_two[0]))
    cv2.imshow('Two sign', sign_two)
    cv2.waitKey()
