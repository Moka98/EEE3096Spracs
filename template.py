#!/usr/bin/python3
"""

Readjust this Docstring as follows:
Names: Moka Mopeli
Student Number: MPLMOK001
Prac: Prac 1
Date:29/07/2019
"""

# import Relevant Librares

import RPi.GPIO as GPIO
import time
import itertools
GPIO.setmode(GPIO.BOARD)
led_list = [11,18,22]
buttons_list = [13,15]
#Enable GPIO pins for LEDS and set them to outputs
GPIO.setup(led_list,GPIO.OUT)
#Enable GPIO pins for buttons and set them to inputs
GPIO.setup(buttons_list,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#Set all the LEDS to be low initially 
GPIO.output(led_list,GPIO.LOW)
outputs =list(itertools.product([0,1],repeat=3))
#Initialize count 
count = 0
# Function for counting up
def countUp(channel):
	print("COUNT UP")
	time.sleep(1)
	global count
	#Present the current value of count to the LEDS
	GPIO.output(led_list,outputs[count])



#Function for counting down
def countDown(channel):
	print("COUNT DOWN")
	time.sleep(1)
	global count
	#Present the current value of count to the LEDS
	GPIO.output(led_list,outputs[count])

        

#Call the countUp function when buttton on channel 13 is pressed
GPIO.add_event_detect(13,GPIO.RISING,callback=countUp,bouncetime = 300)
#Call the countDown function when button on channel 15 is pressed
GPIO.add_event_detect(15,GPIO.RISING,callback=countDown,bouncetime = 300)

def main():
	global count
	#Set count to zero when seven is reached
	if GPIO.event_detected(13):
		if (count==7):
			count =0
		else:
		   count = count +1
	#Set count to seven when zero is reached
	elif GPIO.event_detected(15):
		if (count==0):
			count = 7
		else:
		   count = count - 1
	


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
