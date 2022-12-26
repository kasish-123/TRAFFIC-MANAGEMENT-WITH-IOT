import pyfirmata
import time 
comp='COM11'
board = pyfirmata.Arduino(comp)
led_1=board.get_pin('d:2:o')
led_2=board.get_pin('d:3:o')
led_3=board.get_pin('d:4:o')
led_4=board.get_pin('d:5:o')
led_5=board.get_pin('d:6:o')
led_6=board.get_pin('d:7:o')
l1=[0,0]
def normaltime():
    return 2
def maxtime():
    return 5
def val1():
    return l1[0]
def val2():
    return l1[1]
def signal1():
    l1[0]=1
    l1[1]=0
    led_2.write(0)
    led_5.write(0)
    led_3.write(1)
    led_4.write(1)
def wait():
    l1[0]=0
    l1[1]=0
    led_2.write(1)
    led_3.write(0)
    led_4.write(0)
    led_5.write(1)
    led_1.write(0)
    led_6.write(0)
def signal2():
    l1[0]=0
    l1[1]=1
    led_2.write(0)
    led_6.write(1)
    led_1.write(1)
    led_5.write(0)
def led_norm():
    l1[0]=1
    l1[1]=0
    led_2.write(0)
    led_5.write(0)
    led_3.write(1)
    led_4.write(1)
    time.sleep(5)
    led_2.write(1)
    led_3.write(0)
    led_4.write(0)
    led_5.write(1)
    time.sleep(1)
    l1[0]=1
    l1[1]=0
    led_2.write(0)
    led_6.write(1)
    led_1.write(1)
    led_5.write(0)
    time.sleep(5)
    led_2.write(1)
    led_1.write(0)
    led_6.write(0)
    led_5.write(1)
    time.sleep(1)
def signalmax_1():
    l1[0]=1
    l1[1]=0
    led_2.write(0)
    led_5.write(0)
    led_3.write(1)
    led_4.write(1)
    time.sleep(15)
    led_2.write(1)
    led_3.write(0)
    led_4.write(0)
    led_5.write(1)
    time.sleep(1)
    l1[0]=1
    l1[1]=0
    led_2.write(0)
    led_6.write(1)
    led_1.write(1)
    led_5.write(0)
    time.sleep(15)
    led_2.write(1)
    led_1.write(0)
    led_6.write(0)
    led_5.write(1)
    time.sleep(1)
def signalmax_2():
    l1[0]=1
    l1[1]=0
    led_2.write(0)
    led_5.write(0)
    led_3.write(1)
    led_4.write(1)
    time.sleep(15)
    led_2.write(1)
    led_3.write(0)
    led_4.write(0)
    led_5.write(1)
    time.sleep(1)
    l1[0]=1
    l1[1]=0
    led_2.write(0)
    led_6.write(1)
    led_1.write(1)
    led_5.write(0)
    time.sleep(15)
    led_2.write(1)
    led_1.write(0)
    led_6.write(0)
    led_5.write(1)
    time.sleep(1)