import numpy as np
import cv2

image = cv2.imread('Image3.jpg', 1)
cv2.imshow('image window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()