import opc # opc libray, compatible with the led software
import time # time library

led_colour=[(255,255,255)]*360 # variable 1, led colour for all 360 leds is black. THe background colour remain the same.
led_colour1=[(0,255,0)]*360   #variable 2, led colour for all 360 leds is green. When the leds reaches to the end, green leds shows afterwards.

colours = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'orange': (245,120,66), 'yellow': (245,206,66), 'pink': (245,66,224), 'purple': (185,66,245), 'brown': (102,51,0), 'black': (0,0,0),
 'white': (255,255,255), 'gray': (161,161,161) }  # i define selection of colours so i dont have to enter the number, just colour name is sufficient.


client = opc.Client('localhost:7890')# Calling opc library
sleep = time.sleep # calling time library


def change_led(led_colour): # function for changing in leds colours for first variable
	client.put_pixels(led_colour)
	
led_colour=[(colours.get('black'))]*360
change_led(led_colour)

def x(spec):
	for x in range(len(led_colour)):
		if x == spec:
                    change_led[10] = (0,0,255)
                    sleep(2)
			
			
			

			
welcome = input("Press 1 to open door:")
if welcome == "1":	
	x(0)	
	client.put_pixels(led_colour)
else:
    	print("Door Closed")
sleep(1)

client.put_pixels(led_colour)
client.put_pixels(led_colour)
# if input value 1 is enter then lit leds red colour in first colour which define as 'a'.
# if nothing is detected or fault in entering number, it will say that now airplane has been detected


