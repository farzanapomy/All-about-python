# scan image and display as a gray scale image
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('Digital Image Processing\photo.jpg')
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', image)
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', img_gray)
color = [0, 255, 0]
hard = cv2.copyMakeBorder(img_gray, 60, 60, 50, 60,
                          cv2.BORDER_CONSTANT, value=color)
plt.subplot(224), plt.imshow(hard, 'gray'), plt.title('Hard Border')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
