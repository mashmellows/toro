import cv2
import numpy as np
import matplotlib.pyplot as plt
import win32api, win32con
from PIL import ImageGrab
import time
import win32api
import win32com.client

#TESTING 
goomba = cv2.CascadeClassifier('goomba.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    goom = goomba.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=10, flags=0, minSize=(0, 0))
    
    for (x,y,w,h) in goom:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            goom = goomba.detectMultiScale(roi_gray)

    cv2.imshow('img',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.desotryAllWindows()
