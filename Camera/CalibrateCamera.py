# ____CalibrateCamera.py____
# Author: Mario Ayerra Basés
# Email: marioab09@yahoo.es
# Date: November 8th, 2019
# Description:	Program that calculates the camera parameters and stores them in a text file.
#               Takes all the jpg images in the current folder with the name ImageCalib#. This images are captured with CaptureImages.py
#				https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
#				The name of the file is 'parameters.txt'.
#				If the file already exists, the data will be overwritten.
# Future improvements: better description of each of the parameters
# More info: https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html

import numpy as np
import cv2
from datetime import datetime
import glob

file = open("parameters.txt","w") # Open the file in write mode
now = datetime.now()
file.write(str(now))
file.write('\nCAMERA PARAMETERS:\n________________________')
file.write('\nImages used in the calibration:\n')

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('ImageCalib*.jpg')
print(images)
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
        cv2.imshow('img',img)
        print('Appending the data of '+ fname)
        file.write(fname+'\n')
        cv2.waitKey(500)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

file.write('\n\nret:\n' + str(ret))
file.write('\n\nCamera matrix:\n' + str(mtx))
file.write('\n\nDistortion coefficients (k1, k2, p1, p2[, k3[, k4, k5, k6]])\n' + str(dist))
file.write('\n\nRotation vectors\n' + str(rvecs))        # Don't need this
file.write('\n\nTranslation vectors\n' +str(tvecs))      # Don't need this

file.close()