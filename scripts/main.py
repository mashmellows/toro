import cv2
import numpy as np
import matplotlib.pyplot as plt
import win32api, win32con
from PIL import ImageGrab
import time
import win32api
import win32com.client

m_cactus_cascade = cv2.CascadeClassifier('multi_cactus.xml')
cactus_cascade = cv2.CascadeClassifier('single_cactus.xml')
triple_cac = cv2.CascadeClassifier('triple_cactus.xml')
dual_cac = cv2.CascadeClassifier('dual_cactus.xml')
small_cac = cv2.CascadeClassifier('small_cactus.xml')
end_d = cv2.CascadeClassifier('end.xml')


cap = cv2.VideoCapture(0)


last_time = time.time()

fitness = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    eyes = cactus_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(0, 0))
    m_cac = m_cactus_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(0, 0))
    t_cac = triple_cac.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(0, 0))
    d_cac = dual_cac.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(0, 0))
    s_cac = small_cac.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(0, 0))
    end_det = end_d.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(0, 0))
    
    cv2.rectangle(frame, (0,60), (140, 640), (0,255,0),2)
    
    green_rect_x = 0
    green_rect_x2 = 60
    green_rect_y = range(120,190)
    green_rect_y2 = 640
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Fitness:" + str(fitness),(0,40),font,1, (11,255,255),2, cv2.LINE_AA) 
    
   
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = cactus_cascade.detectMultiScale(roi_gray)





        shell = win32com.client.Dispatch("WScript.Shell")
        if x in green_rect_y or y in green_rect_y:
            shell.SendKeys("{UP}",0)
            print("Jump!")


        
    for (x,y,w,h) in m_cac:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        m_cac = m_cactus_cascade.detectMultiScale(roi_gray)
    



        shell = win32com.client.Dispatch("WScript.Shell")
        if x in green_rect_y or y in green_rect_y:
            shell.SendKeys("{UP}",0)
            print("Jump!")


    for (x,y,w,h) in t_cac:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (128,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            t_cac = triple_cac.detectMultiScale(roi_gray)

            shell = win32com.client.Dispatch("WScript.Shell")
            if x in green_rect_y or y in green_rect_y:
                shell.SendKeys("{UP}",0)
                print("Jump!")

    
    for (x,y,w,h) in d_cac:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            d_cac = dual_cac.detectMultiScale(roi_gray)

            #if x2 in green_rect_y or y2 in green_rect_y:
                #shell.SendKeys("{UP}",0)
                #print("Jump!")

    for (x,y,w,h) in s_cac:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (51,255,230),2)
            roi_gray = gray[y:y+h, x:x+w]
            s_cac = small_cac.detectMultiScale(roi_gray)

            if x in green_rect_y or y in green_rect_y:
                shell.SendKeys("{UP}",0)
                print("Jump!")

    fitness += 1
    
    for (x,y,w,h) in end_det:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (112,0,255),2)
                roi_gray = gray[y:y+h, x:x+w]
                end_det = end_d.detectMultiScale(roi_gray)
                
                if h == 130:
                    shell.SendKeys("{UP}",0)
                    print("RESET")
                

                        
    
    
   
            
    cv2.imshow('img',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.desotryAllWindows()
