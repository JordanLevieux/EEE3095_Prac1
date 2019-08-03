#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Jordan
Student Number: LVXJOR001
Prac: Prac1
Date: 29/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

# Logic that you write
count = 1
#countUp = True

def main():
	#initialise pins
	global count
	outputList = [11,13,15]
	inputList = [29,31]
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(outputList, GPIO.OUT)
	GPIO.setup(inputList, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#add interupts for the inputs
	GPIO.add_event_detect(29, GPIO.FALLING, callback=my_callback_29, bouncetime=400)
	GPIO.add_event_detect(31, GPIO.FALLING, callback=my_callback_31, bouncetime=400)
	
	#update every half second
	while True:
		display(count)
		time.sleep(0.5)

		#Code from when I thought it was supposed to count automatically
		#if countUp == True:
		#	count +=1
		#	if count > 7:
		#		count = 0
		#else:
		#	count -=1
		#	if count<0:
		#		count = 7
		#print (countUp)

#interupts for inputs
def my_callback_29(channel):
	global count
	count += 1
	if count > 7:
		count=0
def my_callback_31(channel):
	global count
	count -= 1
	if count < 0:
		count = 7

#function that creates the output on the LEDs
def display(count):
	for i in range(3):
		GPIO.output(11+2*i, count%2)
		count = count>>1

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
	try:
		GPIO.setwarnings(False)
		while True:
			 main()
	except KeyboardInterrupt:
		print("Exiting gracefully")
		# Turn off your GPIOs here
		GPIO.cleanup()
	except e:
		GPIO.cleanup()
		print("Some other error occurred")
		print(e.message)
