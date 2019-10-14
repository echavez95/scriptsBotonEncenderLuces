import RPi.GPIO as GPIO
import sys
from time import sleep
pin=26 #numero del pin donde esta conectada el foco
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
state = GPIO.input(pin)

if(state is 0):
    #Apagar
    GPIO.output(pin,True)
else:
    #Encender
    GPIO.output(pin,False)

exit(0)

