import RPi.GPIO as GPIO 
import time  

GPIO.setmode(GPIO.BCM)

IN = 17
OUT = 27

GPIO.setup(IN,GPIO.IN)                  
GPIO.setup(OUT,GPIO.OUT)

def metal_detect():
	GPIO.output(OUT, GPIO.HIGH)
	time.sleep(5)
	metal = GPIO.input(IN)
	GPIO.output(OUT, GPIO.LOW)
	return metal