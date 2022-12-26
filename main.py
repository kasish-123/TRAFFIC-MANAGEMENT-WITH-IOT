from vehicle_detection import *
from signals import *
import time
count=1
preval=[]
while True:
    if(count<=2):
        signal1()
        fun1(normaltime())
        wait()
        time.sleep(1)
        signal2()
        fun1(normaltime())
        wait()
        time.sleep(1)
        temp=returnval()
        preval.append(temp)
        count+=1
        print(preval)
    else:
        dif=preval[0][0]-preval[1][0]
        if(dif>=3):
            signal1()
            fun1(maxtime())
        else:
            signal1()
            fun1(normaltime())
        wait()
        time.sleep(1)
        dif=preval[0][1]-preval[1][1]
        if(dif>=1):
            signal2()
            fun1(maxtime())
        else:
            signal2()
            fun1(normaltime())
        wait()
        time.sleep(1)
        preval.pop(0)
        preval.append(returnval())
        print(count)
        print(preval)