import cv2
from matplotlib import pyplot as plt

path = "S:\\CV\\lab2\\lab2-1.jpg"
i = 0
img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_8)
# manual
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# auto
ret_otsu, thresh6 = cv2.threshold(img, 111, 255, cv2.THRESH_OTSU)
ret_triangle, thresh7 = cv2.threshold(img, 111, 255, cv2.THRESH_TRIANGLE)
print('thresh OTSU is %d \nthresh TRIANGLE is %d' % (ret_otsu, ret_triangle))

images = {'Original Image': img, 'BINARY': thresh1, 'BINARY_INV': thresh2, 'TRUNC': thresh3, 'TOZERO': thresh4,
          'TOZERO_INV': thresh5, 'OTSU': thresh6, 'TRIANGLE': thresh7}

for title, image in images.items():
    plt.subplot(2, 4, i + 1), plt.imshow(image, 'gray', vmin=0, vmax=255)
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()

# for titles, images in images.items():
#     cv2.imshow(titles, images)