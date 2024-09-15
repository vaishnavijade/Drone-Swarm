import RPi.GPIO as GPIO
import time

#GPIO Basic initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Use a variable for the Pin to use
#If you followed my pictures, it's port 7 => BCM 4
led = 23
#Initialize your pin
GPIO.setup(led,GPIO.IN)

#Turn on the LED
while True:
  value = GPIO.input(led)
  print(value)
  time.sleep(1)