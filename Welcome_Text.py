import opc # opc libray which communicate with fadecandy
import time # time library

colours = {'black': (0,0,0), 'red': (255,0,0)}# Define these two colours.

client = opc.Client('localhost:7890')# Calling opc library
sleep = time.sleep # calling time library


def change_led(led_colour): # Define function for led colours
	client.put_pixels(led_colour)
	
led_colour=[(colours.get('black'))]*360 # While defining function for the colour, i have to make sure that all 360 leds have similar colour.
change_led(led_colour)

def x(a): # Define function when 'a' is selected, let the funtion turn on the chosen leds.
	for x in range(len(led_colour)):
		if x == a:
			led_colour[x+1] = (colours.get('red'))# Define each single led with its chosen colour.
			led_colour[x+61] = (colours.get('red'))
			led_colour[x+121] = (colours.get('red'))
			led_colour[x+181] = (colours.get('red'))
			led_colour[x+241] = (colours.get('red'))
			led_colour[x+301] = (colours.get('red'))
			led_colour[x+302] = (colours.get('red'))
			led_colour[x+303] = (colours.get('red'))
			led_colour[x+244] = (colours.get('red'))			
			led_colour[x+305] = (colours.get('red'))
			led_colour[x+306] = (colours.get('red'))
			led_colour[x+307] = (colours.get('red'))
			led_colour[x+247] = (colours.get('red'))
			led_colour[x+187] = (colours.get('red'))
			led_colour[x+127] = (colours.get('red'))
			led_colour[x+67] = (colours.get('red'))
			led_colour[x+7] = (colours.get('red'))
			led_colour[x+9] = (colours.get('red'))
			led_colour[x+10] = (colours.get('red'))
			led_colour[x+11] = (colours.get('red'))
			led_colour[x+69] = (colours.get('red'))
			led_colour[x+129] = (colours.get('red'))
			led_colour[x+189] = (colours.get('red'))
			led_colour[x+249] = (colours.get('red'))
			led_colour[x+309] = (colours.get('red'))
			led_colour[x+130] = (colours.get('red'))
			led_colour[x+131] = (colours.get('red'))
			led_colour[x+190] = (colours.get('red'))
			led_colour[x+191] = (colours.get('red'))
			led_colour[x+310] = (colours.get('red'))
			led_colour[x+311] = (colours.get('red'))
			led_colour[x+13] = (colours.get('red'))
			led_colour[x+73] = (colours.get('red'))
			led_colour[x+133] = (colours.get('red'))
			led_colour[x+193] = (colours.get('red'))
			led_colour[x+253] = (colours.get('red'))
			led_colour[x+313] = (colours.get('red'))
			led_colour[x+314] = (colours.get('red'))
			led_colour[x+315] = (colours.get('red'))
			led_colour[x+18] = (colours.get('red'))
			led_colour[x+19] = (colours.get('red'))
			led_colour[x+77] = (colours.get('red'))
			led_colour[x+136] = (colours.get('red'))
			led_colour[x+196] = (colours.get('red'))
			led_colour[x+256] = (colours.get('red'))
			led_colour[x+317] = (colours.get('red'))
			led_colour[x+318] = (colours.get('red'))
			led_colour[x+319] = (colours.get('red'))
			led_colour[x+22] = (colours.get('red'))
			led_colour[x+23] = (colours.get('red'))
			led_colour[x+81] = (colours.get('red'))
			led_colour[x+141] = (colours.get('red'))
			led_colour[x+322] = (colours.get('red'))
			led_colour[x+323] = (colours.get('red'))
			led_colour[x+201] = (colours.get('red'))
			led_colour[x+261] = (colours.get('red'))
			led_colour[x+26] = (colours.get('red'))
			led_colour[x+86] = (colours.get('red'))
			led_colour[x+146] = (colours.get('red'))
			led_colour[x+206] = (colours.get('red'))
			led_colour[x+266] = (colours.get('red'))
			led_colour[x+326] = (colours.get('red'))
			led_colour[x+87] = (colours.get('red'))
			led_colour[x+148] = (colours.get('red'))
			led_colour[x+209] = (colours.get('red'))
			led_colour[x+150] = (colours.get('red'))
			led_colour[x+91] = (colours.get('red'))
			led_colour[x+32] = (colours.get('red'))
			led_colour[x+92] = (colours.get('red'))
			led_colour[x+152] = (colours.get('red'))
			led_colour[x+212] = (colours.get('red'))
			led_colour[x+272] = (colours.get('red'))
			led_colour[x+332] = (colours.get('red'))
			led_colour[x+34] = (colours.get('red'))
			led_colour[x+35] = (colours.get('red'))
			led_colour[x+36] = (colours.get('red'))
			led_colour[x+94] = (colours.get('red'))
			led_colour[x+154] = (colours.get('red'))
			led_colour[x+155] = (colours.get('red'))
			led_colour[x+156] = (colours.get('red'))
			led_colour[x+214] = (colours.get('red'))
			led_colour[x+215] = (colours.get('red'))
			led_colour[x+216] = (colours.get('red'))
			led_colour[x+274] = (colours.get('red'))
			led_colour[x+334] = (colours.get('red'))
			led_colour[x+335] = (colours.get('red'))
			led_colour[x+336] = (colours.get('red'))
			led_colour[x+84] = (colours.get('red'))
			led_colour[x+144] = (colours.get('red'))
			led_colour[x+204] = (colours.get('red'))
			led_colour[x+264] = (colours.get('red'))

#User interface			
welcome = input("Press 1 to show welcome text:") # Define input variable
if welcome == "1":	
	x(0)	
	client.put_pixels(led_colour) # When '1' is selected then show welcome text.
else:
    	print("Try again") # If they dont press '1' then welcome text will be not shown and show 'print("Try again")'.
