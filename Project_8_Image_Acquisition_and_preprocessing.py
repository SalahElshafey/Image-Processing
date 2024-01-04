import cv2
import numpy as np


img =cv2.imread("images/1-Orca.jpg")
blur = cv2.GaussianBlur(img,(5,5),0)



cv2.imshow("Original image",img)
cv2.waitKey(0)

cv2.imshow("Blurred image",blur)
cv2.waitKey(0)

