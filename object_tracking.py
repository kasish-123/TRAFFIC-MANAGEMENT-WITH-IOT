import cv2
import numpy as np
#from signals import *
import time
from object_detection import ObjectDetection
import math
from amb1 import amb
from signals import *
# Initialize Object Detection
od = ObjectDetection()
ab=amb()
l=[0,0]
amblist=[False,False]
valsetamb=False
def valset():
    return valsetamb
def setamb():
    valsetamb=True
def unset():
    valsetamb=False
cap1 = cv2.VideoCapture("dataset/video1.avi")
cap2 = cv2.VideoCapture("test7.mp4")
ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()
def returnval():
    return l[:]
def amb1():
    return amblist[0]
def amb2():
    return amblist[1]
def timerfun(num):
    print(num)
def trackfun(given_time):
    now=time.time()
    timer = 0
    while timer<=given_time:
        count1=0
        count2=0
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break
        # Detect objects on frame
        (class_ids1, scores1, boxes1) = od.detect(frame1)
        (class_ids2, scores2, boxes2) = od.detect(frame2)
        amblist1=ab.detect(frame1)
        amblist2=ab.detect(frame2)
        if(len(amblist1)>0):
            amblist[0]=True
            wait()
            signal1()
            setamb()
            while(len(amblist1)>0):
                print("djgjfv")
                ret1, frame1 = cap1.read()
                if not ret1 or not ret2:
                    break
                amblist1=ab.detect(frame1)
                for i in amblist1:
                    list1=list(map(int,i))
                    (x,y,w,h,c,class1)=list1
                    cx = int((x + x + w) / 2)
                    cy = int((y + y + h) / 2)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    cv2.putText(frame1, "amb", (cx, cy - 10), 0, 1, (0, 0, 255), 2)
                cv2.imshow("Frame1", frame1)
                key = cv2.waitKey(1)
                if key == 27:
                    break
            else:
                wait()
                return
                amblist[0]=False
        if(len(amblist2)>0):
            print("dkjffhriug")
            amblist[1]=True
            wait()
            signal2()
            amb2()
            setamb()
            while(len(amblist2)>0):
                ret2, frame2 = cap2.read()
                amblist1=ab.detect(frame2)
                for i in amblist2:
                    list2=list(map(int,i))
                    (x,y,w,h,c,class1)=list2
                    cx = int((x + x + w) / 2)
                    cy = int((y + y + h) / 2)
                    cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    cv2.putText(frame2, "amb", (cx, cy - 10), 0, 1, (0, 0, 255), 2)
                cv2.imshow("Frame2", frame2)
                key = cv2.waitKey(1)
                if key == 27:
                    break
            else:
                wait()
                return
                amblist[1]=False
        for box in boxes1:
            count1 += 1
            (x, y, w, h) = box
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame1, (cx,cy), 5, (0, 0, 255), -1)
            cv2.putText(frame1, str(count1), (cx, cy - 7), 0, 1, (0, 0, 255), 2)
        for box in boxes2:
            count2 += 1
            (x, y, w, h) = box
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame2, (cx,cy), 5, (0, 0, 255), -1)
            cv2.putText(frame2, str(count2), (cx, cy - 7), 0, 1, (0, 0, 255), 2)

        cv2.imshow("Frame1", frame1)
        cv2.imshow("Frame2", frame2)
#        if(val1()==0):
#            l[0]=count1
#        if(val2()==0):
#            l[1]=count2
        

        key = cv2.waitKey(1)
        if key == 27:
            break
        end = time.time()
        timer = round(end-now)
        print(timer)

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()
#trackfun(6)