# ____Undistort.py____
# Author: Mario Ayerra Basés
# Email: marioab09@yahoo.es
# Date: November 22th, 2019
# Description: 	The program uses the parameters calculated by CalibrateCamera.py
#				It opens one of the images (in this case ImageCalib4.jpg) and undistorts it. The new image is saved. 

import cv2
import numpy as np

# Camera matrix:
mtx = np.array([[313.11759812, 0., 317.56209254],[0., 312.61044503, 231.97210137], [0., 0., 1.]])

# Distortion coefficients:
dist = np.array([[ 0.04781336, -0.10113369, -0.00107591, 0.00079112, 0.04188298]])
# k1 = 0.04781336
# k2 = -0.10113369
# p1 = -0.00107591
# p2 = 0.00079112
# k3 = 0.04188298

# Translation vector:
tvec = np.array([[-3.62385681, -2.50091863, 5.51081908]])
# Rotation vector: 
rvec = np.array([[-0.13685726, 0.0755823, -0.03845367]])

# Refine the camera matrix based on a free scaling parameter
img = cv2.imread('ImageCalib4.jpg')   #CHANGE THIS TO THE NAME OF THE IMAGE YOU WANT TO UNDISTORT
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# Undistort
img_undist = cv2.undistort(img, mtx, dist, None, newcameramtx)

# Crop the image
x,y,w,h = roi
img_undist = img_undist[y:y+h, x:x+w]
cv2.imwrite('undistorted_Image4.jpg',img_undist)
