import opc
import time 

led_colour=[(255,255,255)]*360 
led_colour1=[(0,255,0)]*360   
led_colour2=[(0,0,255)]*360



colours = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'orange': (245,120,66), 'yellow': (245,206,66), 'pink': (245,66,224), 'purple': (185,66,245), 'brown': (102,51,0), 'black': (0,0,0),
 'white': (255,255,255), 'gray': (161,161,161) }  


client = opc.Client('localhost:7890')
sleep = time.sleep

     



def change_led(led_colour):
	client.put_pixels(led_colour)
	
led_colour=[(colours.get('black'))]*360
change_led(led_colour)

def change_led1(led_colour1): 
	client.put_pixels(led_colour)
	
led_colour1=[(colours.get('black'))]*360
change_led1(led_colour1)

def change_led2(led_colour2): 
	client.put_pixels(led_colour2)
	
led_colour2=[(colours.get('green'))]*360
change_led2(led_colour2)

def change_led3(led_colour3): 
	client.put_pixels(led_colour3)
	
led_colour3=[(colours.get('blue'))]*360
change_led3(led_colour3)

def change_led4(led_colour4): 
	client.put_pixels(led_colour4)
	
led_colour4=[(colours.get('pink'))]*360
change_led4(led_colour4)

def change_led5(led_colour5): 
	client.put_pixels(led_colour5)
	
led_colour5=[(colours.get('purple'))]*360
change_led5(led_colour5)

def change_led6(led_colour6): 
	client.put_pixels(led_colour6)



	
	
led_colour6=[(colours.get('white'))]*360
change_led6(led_colour6)



def main(): 
    	while True: 
    		prompt_user() 


def prompt_user():
        selection=input("enter no whose table you want:")
if a == selection:
	for uw in range (0,19):
     for uw1 in range(0,6):
        calci[uw+60*uw1] = (255,255,52)#light yellow for underweight
  	print(selection) 

if __name__ == '__main__': main() 
