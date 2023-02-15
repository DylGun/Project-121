import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)
image = cv2.imread("output.jpeg")


while True:
    ret, frame = video.read()
    frame=cv2.resize(frame, (640,480))
    
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask1 = cv2.inRange(frame,l_black,u_black)

    mask = cv2.inRange(frame,l_black,u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f=frame - res
    f=np.where(f == 0, image, f)