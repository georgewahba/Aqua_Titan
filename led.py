import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led = 5
led2 = 16

GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

while True:
    GPIO.output(led, True)
    sleep(1)
    GPIO.output(led2, True)
    GPIO.output(led, False)
    sleep(1)
    GPIO.output(led2, False)