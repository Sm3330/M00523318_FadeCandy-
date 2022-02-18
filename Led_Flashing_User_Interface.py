import opc # Import opc library to communicate with FadeCandy
import time # Time library is imported

led_colour0=[(153,0,0)]*360 # Define list of 6 different colours here.
led_colour1=[(153,76,0)]*360   
led_colour2=[(153,153,0)]*360
led_colour2=[(76,153,0)]*360
led_colour3=[(0,153,0)]*360
led_colour4=[(0,153,76)]*360
led_colour5=[(0,76,153)]*360
led_colour6=[(76,0,153)]*360

colours = {'black': (0,0,0)}  # Define colour for the background here


client = opc.Client('localhost:7890')# Calling opc library
sleep = time.sleep # Calling time library


def change_led(led_colour): # Define function for background colour of the leds before leds begins to flash.
	client.put_pixels(led_colour)
	
led_colour=[(colours.get('black'))]*360 # Select the colour here and apply to all 360 leds.
change_led(led_colour)

#User Interface			
Do_you_want_Leds_to_Turn_ON = input("Press y to turn on leds or n to keep it turn off:") # Define Input here by asking user whethere they want turn on leds or not by entering y/n.
if Do_you_want_Leds_to_Turn_ON == "y":
        client.put_pixels(led_colour0)
        sleep(1)
        client.put_pixels(led_colour1)
        sleep(1)
        client.put_pixels(led_colour2)
        sleep(1)
        client.put_pixels(led_colour3)
        sleep(1)
        client.put_pixels(led_colour4)
        sleep(1)
        client.put_pixels(led_colour5)
        sleep(1)
        client.put_pixels(led_colour6)
        sleep(1)
        client.put_pixels(led_colour0)
        sleep(1)
        client.put_pixels(led_colour1)
        sleep(1)
        client.put_pixels(led_colour2)
        sleep(1)
        client.put_pixels(led_colour3)
        sleep(1)
        client.put_pixels(led_colour4)
        sleep(1)
        client.put_pixels(led_colour5)
        sleep(1)
        client.put_pixels(led_colour6)
        sleep(1)
	
elif Do_you_want_Leds_to_Turn_On == "n": # When n is enter then the leds will kept turn and a message will be printed "print("Leds are kept OFF")".
        print("Leds are kept OFF")
        sleep(1)




