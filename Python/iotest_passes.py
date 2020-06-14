import RPi.GPIO as GPIO
import time

LIGHT_SENSOR_PIN=25
#LED_PIN=18
RUN_SECONDS=5.0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

timeStarted = False
timeElapsed = False

startTime = 0.0
passesDetected = 0.0
lastState = GPIO.input(LIGHT_SENSOR_PIN)
print ("initial latch state, ", lastState)

while not timeElapsed:
    #Once the input changes from the inital value, start the timer    
    pinState = GPIO.input(LIGHT_SENSOR_PIN)
        
    if lastState != pinState and not timeStarted:
        timeStarted = True
        #initialize start time to the current time in seconds
        startTime = time.time()
        print ("Timer starting value: ", startTime);

    if timeStarted and pinState != lastState: 
        passesDetected += 1.0
        lastState = pinState
        print("resetting pin state")
    
    if timeStarted:
        timeElapsed = ((time.time() - startTime) > RUN_SECONDS)
            
    
print ("total passes = ", passesDetected / 2)
print ("average passes per second = ", passesDetected / 2 / RUN_SECONDS)
