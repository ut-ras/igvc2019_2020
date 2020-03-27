# ____CaptureImages.py____
# Author: Mario Ayerra Basés
# Email: marioab09@yahoo.es
# Date: November 8th, 2019
# Description: 	The program opens an external camera and saves pictures when pressing the 'c' key on the keyboard.
#				The images are stored under the name 'ImageCalib#.jpg'. This can be changed in line 15.
#				Press the key 'q' to quit

import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 (or -1) for the main camera. 1 to select a second camera. Try 2 for the USB camera

im_num = 0
im_name_base = 'ImageTest'
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'): #Press q to quit
        break
    elif key_pressed == ord('c'): #Press c to capture
        im_num += 1
        im_name = im_name_base + str(im_num) + '.jpg'
        # Save image in the current directory
        cv2.imwrite(im_name,frame) 
        print('Image {} saved'.format(im_num))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
