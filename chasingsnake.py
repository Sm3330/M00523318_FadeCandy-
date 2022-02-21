import opc
from time import sleep
import sys

led_colour=[(255,0,0)]*360

colours = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'orange': (245,120,66), 'yellow': (245,206,66), 'pink': (245,66,224), 'purple': (185,66,245), 'brown': (102,51,0), 'black': (0,0,0),
 'white': (255,255,255), 'gray': (161,161,161) }

client = opc.Client('localhost:7890')


def update_led(led_colour):
	client.put_pixels(led_colour)

led_colour=[(colours.get('black'))]*360
update_led(led_colour)


def chasing_snake(colour,increase,slept):
	for x in range(0,360,increase):
		led_colour[x] = (colours.get('black'))
		client.put_pixels(led_colour)
		sleep(0.05)

		led_colour[x-360] = (colours.get('white'))
		client.put_pixels(led_colour)
		sleep(0.005)

		led_colour[x+3] = (colours.get('black'))
		client.put_pixels(led_colour)
		sleep(0.005)

		led_colour[x+4] = (colours.get('red'))
		client.put_pixels(led_colour)
		sleep(0.005)

		led_colour[x+1] = (colours.get('green'))
		client.put_pixels(led_colour)
		sleep(0.005)

	
		client.put_pixels(led_colour)
		sleep(0.09)
		
		


chasing_snake('red', 1, 5)


