import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

def print_rising(ev=None):
    print('RISING')

def print_falling(ev=None):
    print('FALLING')


GPIO.add_event_detect(18, GPIO.FALLING, callback=print_rising, bouncetime=100)
# GPIO.add_event_detect(18, GPIO.RISING, callback=print_falling, bouncetime=100)

while True:
    time.sleep(1)