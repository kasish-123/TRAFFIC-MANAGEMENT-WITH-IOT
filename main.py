#from object_tracking import *
from vehicle_detection import *
from signazkls import *
import time
count=1
preval=[]
while True:
    if(count<=2):
sz        signal1()
        trackfun(normaltime())
        print("kdjfhf",valset())
        if(valset()):
            unset()
            print("signal1")
            continue
        wait()
        time.sleep(1)
        signal2()
        trackfun(normaltime())
        if(valset()):
            unset()
            print("signal2")
            continue
        wait()
        time.sleep(1)
        temp=returnval()
        preval.append(temp)
        count+=1
        print("hdf")
        print(preval)
    else:
        dif=preval[1][0]-preval[0][0]
        if(dif>=2):
            signal1()
            trackfun(maxtime())
        else:
            signal1()
            trackfun(normaltime())
        if(valset()):
            unset()
            count=1
            continue
        wait()
        time.sleep(1)
        dif=preval[1][1]-preval[0][1]
        if(dif>=3):
            signal2()
            trackfun(maxtime())
        else:
            signal2()
            trackfun(normaltime())
        if(valset()):
            unset()
            count=1
            preval=[]
            continue
        wait()
        time.sleep(1)
        preval.pop(0)
        preval.append(returnval())
        #print(count)
        print(preval)
