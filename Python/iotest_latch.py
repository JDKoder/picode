import RPi.GPIO as GPIO
import Latches
import time

BUTTON_PIN=25
LED_PIN=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUTTON_PIN, GPIO.IN)

    
while True:
#    Latches.simpleLatch(BUTTON_PIN)
     Latches.analogueLatch(BUTTON_PIN)
#    Latches.delayedLatch(BUTTON_PIN, 60*6)
     GPIO.output(LED_PIN, Latches.getSignal())
