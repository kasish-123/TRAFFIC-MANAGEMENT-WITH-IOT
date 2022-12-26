import cv2
from signals import *
import time
cascade_src = 'cars.xml'
video_src = 'dataset/test2.mp4'
video_src1 = 'dataset/test3.mp4'
l=[0,0]
cap = cv2.VideoCapture("dataset/test2.mp4")
cap1 = cv2.VideoCapture("dataset/test3.mp4")
car_cascade = cv2.CascadeClassifier(cascade_src)
ret, img = cap.read()
ret1,img1 = cap1.read()
num=0
def returnval():
    return l[:]
def fun1(time1):
    now=time.time()
    timer = 0
    while timer<=time1:
        ret, img = cap.read()
        ret1,img1 = cap1.read()
        if (type(img) == type(None)):
            break
        if(type(img1)==type(None)):
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('video', gray)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        cars1 = car_cascade.detectMultiScale(gray1, 1.1, 1)
        for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        for (x,y,w,h) in cars1:
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('video', img)
        cv2.imshow('video1', img1)
        if(val1()==0):
            l[0]=len(cars)
        if(val2()==0):
            l[1]=len(cars1)
        if cv2.waitKey(33) == 27:
            break
        end = time.time()
        timer = round(end-now)
        print(timer)
    cv2.destroyAllWindows()
        #return num