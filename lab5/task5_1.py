# Протестировать работу оператора Собеля на изображениях клетки и косой штриховки. Протестировать работу фильтра Лапласа на тех же изображениях.
import cv2
from matplotlib import pyplot as plt

i = 0
path_cage = 'S:\\CV\\lab5\\cage_lines.jpeg'
path_oblique = 'S:\\CV\\lab5\\oblique_lines.jpg'
img_cage = cv2.imread(path_cage, cv2.IMREAD_REDUCED_GRAYSCALE_4)
img_oblique = cv2.imread(path_oblique, cv2.IMREAD_GRAYSCALE)

# Sobel dx=0,dy=1
sobel_img_cage_y1 = cv2.Sobel(img_cage, cv2.CV_8U, dx=0, dy=1, ksize=3)
sobel_img_oblique_y1 = cv2.Sobel(img_oblique, cv2.CV_8U, dx=0, dy=1, ksize=3)
# dx=1,dy=0
sobel_img_cage_x1 = cv2.Sobel(img_cage, cv2.CV_8U, dx=1, dy=0, ksize=3)
sobel_img_oblique_x1 = cv2.Sobel(img_oblique, cv2.CV_8U, dx=1, dy=0, ksize=3)
#
sobel = {'img_cage': img_cage, 'sobel_img_cage_y1': sobel_img_cage_y1, 'sobel_img_cage_x1': sobel_img_cage_x1,
         'img_oblique': img_oblique, 'sobel_img_oblique_y1': sobel_img_oblique_y1,
         'sobel_img_oblique_x1': sobel_img_oblique_x1}

fig1 = plt.figure('sobel', figsize=(10, 7))
for title, image in sobel.items():
    fig1.add_subplot(2, 3, i + 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    i += 1
    # cv2.imshow(title, image)
i = 0

# laplacian
laplace_img_cage = cv2.Laplacian(img_cage, -1, ksize=3)
laplace_img_oblique = cv2.Laplacian(img_oblique, -1, ksize=3)


laplace = {'img_cage': img_cage, 'laplace_img_cage': laplace_img_cage, 'img_oblique': img_oblique,
           'laplace_oblique': laplace_img_oblique}
fig2 = plt.figure('laplace', figsize=(10, 7))
for title, image in laplace.items():
    fig2.add_subplot(2, 2, i + 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    i += 1
    # cv2.imshow(title, image)
plt.show()
i = 0
