import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

iterator = 50
#turn the output on and off 5 times
while iterator > 0:
    print(iterator)
    print("GPIO.output(18, TRUE)")
    GPIO.output(18, True)
    time.sleep(1)
    print("GPIO.output(18, FALSE)")
    GPIO.output(18, False)
    time.sleep(1)
    iterator -= 1
    