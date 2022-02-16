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
			led_colour[x+1] = (colours.get('red'))
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


