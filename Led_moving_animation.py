import opc #opc library imported which allows to communicate with Fadecandy
from time import sleep # Time and sleep Library

#Define the led colour for the background
led_colour=[(245, 126, 66),(245, 126, 66),(245, 126, 66),(0,0,0),(0,0,0),(0,0,0)]*91
led_colour1=[(0, 0, 0),(0, 0, 0),(0, 0, 0),(245, 126, 66),(245, 126, 66),(245, 126, 66)]*91
led_colour2=[(66, 245, 96),(66, 245, 96),(66, 245, 96),(0,0,0),(0,0,0),(0,0,0)]*91
led_colour3=[(0, 0, 0),(0, 0, 0),(0, 0, 0),(66, 188, 245),(66, 188, 245),(66, 188, 245)]*91


client = opc.Client('localhost:7890')



client.put_pixels(led_colour) #Let Leds have chosen Led_colour from the list.
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)

client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)

client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)


client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)

client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)

client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)

client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)

client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)
client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)

client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)
client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)
client.put_pixels(led_colour)
sleep(0.2)

client.put_pixels(led_colour1)
sleep(0.2)
