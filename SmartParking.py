
import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)

trigS1 = 3
trigS2 = 5
trigS3 = 7
trigS4 = 11
trigS5 = 13
trigS6 = 15
echoS1 = 19
echoS2 = 21
echoS3 = 23
echoS4 = 29
echoS5 = 31
echoS6 = 33

distance1 = 0
distance2 = 0
distance3 = 0
distance4 = 0
distance5 = 0
distance6 = 0

status1 = ""
status2 = ""
status3 = ""
status4 = ""
status5 = ""
status6 = ""

GPIO.setup(trigS1 , GPIO.OUT)
GPIO.setup(trigS2 , GPIO.OUT)
GPIO.setup(trigS3 , GPIO.OUT)
GPIO.setup(trigS4 , GPIO.OUT)
GPIO.setup(trigS5 , GPIO.OUT)
GPIO.setup(trigS6 , GPIO.OUT)
GPIO.setup(echpS1 , GPIO.IN)
GPIO.setup(echpS2 , GPIO.IN)
GPIO.setup(echpS3 , GPIO.IN)
GPIO.setup(echpS4 , GPIO.IN)
GPIO.setup(echpS5 , GPIO.IN)
GPIO.setup(echpS6 , GPIO.IN)

def FindDistance1():
    
    GPIO.output(trigS1 , False)
    time.sleep(1)
    GPIO.output(trigS1 , True)
    time.sleep(0.00001)
    GPIO.output(trigS1, False)
    while GPIO.input(echoS1)==0:
        pulse_start = time.time()
    while GPIO.input(echoS1)==1:
        pulse_end = time.time()

    pulse = pulse_end - pulse_start
    distance1 = pulse * 17150
    distance1 = round(distance , 2)
    if distance1 < 10 :
        distance1 = 1
        status1 =  "slot 1 is full"
        return distance1
        
    else:
        distance1 = 0
        status1 =  "slot 1 is empty"
        return distance1
    
    return status1
def FindDistance2():
    
    GPIO.output(trigS2 , False)
    time.sleep(1)
    GPIO.output(trigS2 , True)
    time.sleep(0.00001)
    GPIO.output(trigS2, False)
    while GPIO.input(echoS1)==0:
        pulse_start = time.time()
    while GPIO.input(echoS2)==1:
        pulse_end = time.time()

    pulse = pulse_end - pulse_start
    distance2 = pulse * 17150
    distance2 = round(distance , 2)
    if distance2 < 10 :
        distance2 = 1
        status2 =  "slot 2 is full"
        return distance2
        
    else:
        distance2 = 0
        status2 =  "slot 2 is empty"
        return distance2
    
    return status2

def FindDistance3():
        
    GPIO.output(trigS3 , False)
    time.sleep(1)
    GPIO.output(trigS3 , True)
    time.sleep(0.00001)
    GPIO.output(trigS3, False)
    while GPIO.input(echoS3)==0:
        pulse_start = time.time()
    while GPIO.input(echoS3)==1:
        pulse_end = time.time()

    pulse = pulse_end - pulse_start
    distance3 = pulse * 17150
    distance3 = round(distance , 2)
    if distance3 < 10 :
        distance3 = 1
        status3 =  "slot 3 is full"
        return distance3
        
    else:
        distance3 = 0
        status3 =  "slot 3 is empty"
        return distance3
    
    return status3
    
    

def FindDistance4():
    
       
    GPIO.output(trigS4 , False)
    time.sleep(1)
    GPIO.output(trigS4 , True)
    time.sleep(0.00001)
    GPIO.output(trigS4, False)
    while GPIO.input(echoS4)==0:
        pulse_start = time.time()
    while GPIO.input(echoS4)==1:
        pulse_end = time.time()

    pulse = pulse_end - pulse_start
    distance4 = pulse * 17150
    distance4 = round(distance , 2)
    if distance4 < 10 :
        distance4 = 1
        status4 =  "slot 4 is full"
        return distanc4
        
    else:
        distance4 = 0
        status4 =  "slot 4 is empty"
        return distance4
    
    return status4

def FindDistance5():
    
        
    GPIO.output(trigS5 , False)
    time.sleep(1)
    GPIO.output(trigS5 , True)
    time.sleep(0.00001)
    GPIO.output(trigS5, False)
    while GPIO.input(echoS5)==0:
        pulse_start = time.time()
    while GPIO.input(echoS5)==1:
        pulse_end = time.time()

    pulse = pulse_end - pulse_start
    distance5 = pulse * 17150
    distance5 = round(distance , 2)
    if distance5 < 10 :
        distance5 = 1
        status5 =  "slot 5 is full"
        return distance5
        
    else:
        distance5 = 0
        status5 =  "slot 5 is empty"
        return distance5
    
    return status5
def FindDistance6():
    
        
    GPIO.output(trigS6 , False)
    time.sleep(1)
    GPIO.output(trigS6 , True)
    time.sleep(0.00001)
    GPIO.output(trigS6, False)
    while GPIO.input(echoS6)==0:
        pulse_start = time.time()
    while GPIO.input(echoS6)==1:
        pulse_end = time.time()

    pulse = pulse_end - pulse_start
    distance6 = pulse * 17150
    distance6 = round(distance , 2)
    if distance6 < 10 :
        distance6 = 1
        status6 =  "slot 6 is full"
        return distance6
        
    else:
        distance6 = 0
        status6 =  "slot 6 is empty"
        return distance6
    
    return status6


while True:
    FindDistance1()
    FindDistance2()
    FindDistance3()
    FindDistance4()
    FindDistance5()
    FindDistance6()
    count = distance1 + distance2+ distance3 + distance4 + distance5 + distance6
    empty = 6 - count
    print(count +"is the number of slots full" + "" + empty + "is the number of slots empty ")
    print(status1 + "" + status2 + "" + status3 + "" + status4 + "" + status5 + "" + status6)
    time.sleep(10)    
        
