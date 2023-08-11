import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os
import matplotlib.image as mpimg
from easyocr import Reader
class amb:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5','custom',path='best.pt',force_reload=True,trust_repo=True)
    def detect(self,frame):
        results = self.model(frame)
        i=results.xyxy[0]
        l=i.tolist()
        print(l)
        return l

"""model = torch.hub.load('ultralytics/yolov5','custom',path='best.pt',force_reload=True,trust_repo=True)
cap = cv2.VideoCapture("test7.mp4")

while cap.isOpened():
        ret,frame = cap.read()

        # Make detections 
        results = model(frame)

        #cv2.imshow('YOLO', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        #cv2.imshow('YOLO', np.squeeze(results.render()))
        for i in results.xyxy:
            print(i)
            (x,y,w,h,c,class1)=list(map(int,i.tolist()[0]))
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            print(x,y,w,h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.imshow("Frame1", frame)
                
cap.release()
cv2.destroyAllWindows()"""