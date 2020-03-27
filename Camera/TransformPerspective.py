import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Image3.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[307, 167],[359, 167],[0, 336],[640, 336]]) #Find this points manually
pts2 = np.float32([[0,0],[640,0],[0,336],[640, 336]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(640, 370))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
