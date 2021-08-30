import RPi.GPIO as GPIO                   
import time            
from capture_image import * 
from process_db import *
from process_iamge import *  
from voice_alert import * 
from send_message import * 
from metal_detect import *   
                
GPIO.setmode(GPIO.BCM)                      

TRIG1 = 23                                 
ECHO1 = 24 
TRIG2 = 14                                 
ECHO2 = 15  
POWER = 5                                

GPIO.setup(TRIG1,GPIO.OUT)                  
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)                  
GPIO.setup(ECHO2,GPIO.IN)  
GPIO.setup(POWER,GPIO.OUT)                 

while True:

	GPIO.output(TRIG1, False)                 
	print "Waitng For Sensor To Settle"
	time.sleep(2)                            

	GPIO.output(TRIG1, True)                  
	time.sleep(0.00001)                      
	GPIO.output(TRIG1, False)                 

	while GPIO.input(ECHO1)==0 :              
		pulse_start1 = time.time() 

	while GPIO.input(ECHO2)==0 :              
		pulse_start2 = time.time()              

	while GPIO.input(ECHO1)==1 :               
		pulse_end1 = time.time()

	while GPIO.input(ECHO2)==1 :               
		pulse_end2 = time.time()                

	pulse_duration1 = pulse_end1 - pulse_start1 
	pulse_duration2 = pulse_end2 - pulse_start2 

	distance1 = pulse_duration1 * 17150        
	distance1 = round(distance1, 2)  

	distance2 = pulse_duration2 * 17150        
	distance2 = round(distance2, 2)            

	if distance1 > 2 and distance1 < 400  && distance2 == 0 :      
		print "person detected outside entrance" 
		capture_image()
		process_db()
		who = process_image()
		voice_alert_ID(who)
		metal = metal_detect()
		metal_alert(metal)
		if who != 'unknown' :
			voice_alert_ask()
			command = def listen_command()

			while (command != 'yes' && command != 'no')
				say_again()
				command = def listen_command()

			if command == 'yes':
				GPIO.output(led_pin, GPIO.HIGH)
				voice_alert_enter()
				time.sleep(5)
				GPIO.output(led_pin, GPIO.LOW)
				voice_alert_close()
				break

			elif command == 'no':
				voice_alert_deny()
				break

	elif distance2 != 0 :
		send_message()			
		
                     