import cv2
from matplotlib import pyplot as plt

path = 'S:\\CV\\lab2\\emoji.jpg'
i = 0
img = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_4)
adaptive1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 5)
adaptive2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 4)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
images = {'Original Image': img, 'Global Thresholding': thresh, 'Adaptive Mean Thresholding': adaptive1,
          'Adaptive Gaussian Thresholding': adaptive2}

for title, image in images.items():
    plt.subplot(1, 4, i + 1), plt.imshow(image, 'gray', vmin=0, vmax=255)
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()

# for title, image in images.items():
#     cv2.imshow(title, image)
# cv2.waitKey()

# # debug
# for i in range(10):
#     adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, i)
#     cv2.imshow('win' + str(i), adaptive)
#     key = cv2.waitKey()
#     if key == ord('q'):
#         break
#     cv2.destroyAllWindows()
