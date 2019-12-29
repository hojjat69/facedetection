# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# loading opencv2
import cv2
# making a cascade for eyes and faces
face_Cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_Cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect(gray, frame):
    faces = face_Cascade.detectMultiScale(gray, 1.3,5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        roi_gray =gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_Cascade.detectMultiScale(roi_gray, 1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0),2)
    return frame 
video_capture=cv2.VideoCapture(0)
while(True):
    _,frame = video_capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result=detect(gray, frame)
    cv2.imshow('result', result)
    k=cv2.waitKey(1) & 0XFF
    if k==() :
        break
video_capture.release()
cv2.destroyAllWindows()
    
       
        
        