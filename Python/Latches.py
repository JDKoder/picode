import RPi.GPIO as GPIO
import time

inverter = -1
lowHigh = {1: GPIO.HIGH, -1:GPIO.LOW}
latch = False

#A latch that should only be controlled digitally since analogue input is
#not reliably fast enough to keep from constant input.
def simpleLatch(inputPin):
    global inverter
    if not GPIO.input(inputPin):
        print("inverter value i: ", inverter)
        inverter *= -1
        print("inverter value o: ", inverter)

#allows constant input to invert the signal after a period of time in seconds specified by delay
def delayedLatch(inputPin, delay):
    global inverter
    if not GPIO.input(inputPin):
        print("inverter value i: ", inverter)
        inverter *= -1
        print("inverter value o: ", inverter)
        print("delaying ", delay, " seconds before alowing input.")
        time.sleep(delay)

#A latch that allows analogue input (such as pressing a button) to not change until the next time the
#input is activated.
def analogueLatch(inputPin):
    global latch
    global inverter
    if not GPIO.input(inputPin) and latch==False:
        print("inverter value: ", inverter)
        inverter *= -1
        latch = True
        print("Latched: ", latch)
    elif GPIO.input(inputPin) and latch==True:
        latch = False
        print("Latched: ", latch)
    return latch
        
def getSignal():
    global lowHigh
    global inverter
    return lowHigh[inverter]