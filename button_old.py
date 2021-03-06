#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os

def main():

    # tell the GPIO module that we want to use the 
    # chip's pin numbering scheme
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    
    # setup pin 25 as an output
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.OUT) # red
    GPIO.setup(25,GPIO.OUT) # green
    GPIO.setup(27,GPIO.OUT) # yellow
    
    timerVal = 0.5

    # Initiate sequence
    GPIO.output(24,True)
    time.sleep(timerVal)
    GPIO.output(27,True)
    time.sleep(timerVal)
    GPIO.output(25,True)
    time.sleep(timerVal)
    GPIO.output(24,False)
    time.sleep(timerVal)
    GPIO.output(27,False)
    time.sleep(timerVal)
    GPIO.output(25,False)
    
    while True:
        if GPIO.input(23):
             # the button is being pressed, so turn on the green LED
             # and turn off the red LED
             GPIO.output(24,False)
             GPIO.output(25,False)
             
        else:
             # the button isn't being pressed, so turn off the green LED
             # and turn on the red LED
             GPIO.output(24,False)
             
             time.sleep(timerVal)
             GPIO.output(24,True)
             print 3
             time.sleep(timerVal)
             GPIO.output(24,False)
             time.sleep(timerVal)
             GPIO.output(27,True)
             print 2
             time.sleep(timerVal)
             GPIO.output(27,False)
             time.sleep(timerVal)
             GPIO.output(25,True)
             print 1
             time.sleep(timerVal)
             GPIO.output(25,False)
             time.sleep(timerVal/2)
             #GPIO.output(25,True)
             print "button true"
             print "taking photo....."
             time.sleep(timerVal)
             ts = time.time()
             os.system("raspistill -o image" + str(ts)+".jpg -t 1 -n -h 612 -w 612")
             print "photo taken...."
             print "reset....."
             GPIO.output(24,True)
             time.sleep(timerVal/4)
             GPIO.output(24,False)
             time.sleep(timerVal/4)
             GPIO.output(24,True)
             time.sleep(timerVal/4)
             GPIO.output(24,False)
        time.sleep(0.1)
        
    print "button pushed"

    GPIO.cleanup()



if __name__=="__main__":
    main()

