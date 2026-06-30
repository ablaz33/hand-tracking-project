import cv2
import time
import numpy as np


################
wCam, hCam = 640, 480 
################
#check if the webcam is working
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0;
while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX,
                0.7, (255, 0, 0), 2)
    cv2.imshow("Img", img)
    cv2.waitKey(1)