import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

while True:
    #turn off the led when button is high
    if GPIO.input(25):
        print("GPIO.output(18, FALSE")
        GPIO.output(18, False)
    else:
        print("GPIO.output(18, TRUE")
        GPIO.output(18, True)