#coding=utf-8

import cv2
import numpy as np

img = cv2.imread("img/ag.png")

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

img = img[:, :, 0]

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()