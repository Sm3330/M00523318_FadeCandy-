import opc # opc libray, compatible with the led software
import time # time library

led_colour=[(255,255,255)]*360 # variable 1, led colour for all 360 leds is black. THe background colour remain the same.
led_colour1=[(0,255,0)]*360   #variable 2, led colour for all 360 leds is green. When the leds reaches to the end, green leds shows afterwards.
led_colour2=[(0,0,255)]*360



colours = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'orange': (245,120,66), 'yellow': (245,206,66), 'pink': (245,66,224), 'purple': (185,66,245), 'brown': (102,51,0), 'black': (0,0,0),
 'white': (255,255,255), 'gray': (161,161,161) }  # i define selection of colours so i dont have to enter the number, just colour name is sufficient.


client = opc.Client('localhost:7890')# Calling opc library
sleep = time.sleep # calling time library


def change_led(led_colour): # function for changing in leds colours for first variable
	client.put_pixels(led_colour)
	
led_colour=[(colours.get('black'))]*360
change_led(led_colour)

def change_led1(led_colour1): # function for changing in leds colours for first variable
	client.put_pixels(led_colour)
	
led_colour1=[(colours.get('blue'))]*360
change_led1(led_colour1)


def change_led2(led_colour2): # function for changing in leds colours for first variable
	client.put_pixels(led_colour2)
	
led_colour2=[(colours.get('blue'))]*360
change_led2(led_colour2)


def a(spec):
	for a in range(len(led_colour1)):
		if a == spec:
			led_colour1[a+4] = (colours.get('white'))
			led_colour1[a+63] = (colours.get('white'))
			led_colour1[a+64] = (colours.get('white'))			
			led_colour1[a+65] = (colours.get('white'))
			led_colour1[a+122] = (colours.get('white'))
			led_colour1[a+123] = (colours.get('white'))
			led_colour1[a+124] = (colours.get('white'))
			led_colour1[a+125] = (colours.get('white'))
			led_colour1[a+126] = (colours.get('white'))
			led_colour1[a+183] = (colours.get('white'))
			led_colour1[a+184] = (colours.get('white'))
			led_colour1[a+185] = (colours.get('white'))
			led_colour1[a+242] = (colours.get('white'))
			led_colour1[a+243] = (colours.get('white'))
			led_colour1[a+244] = (colours.get('white'))
			led_colour1[a+245] = (colours.get('white'))
			led_colour1[a+246] = (colours.get('white'))
			led_colour1[a+304] = (colours.get('white'))
			led_colour1[a+241] = (colours.get('white'))
			led_colour1[a+247] = (colours.get('white'))
def aa(spec):
	for aa in range(len(led_colour)):
		if aa == spec:
			led_colour[aa+4] = (colours.get('white'))
			led_colour[aa+63] = (colours.get('white'))
			led_colour[aa+64] = (colours.get('white'))			
			led_colour[aa+65] = (colours.get('white'))
			led_colour[aa+122] = (colours.get('white'))
			led_colour[aa+123] = (colours.get('white'))
			led_colour[aa+124] = (colours.get('white'))
			led_colour[aa+125] = (colours.get('white'))
			led_colour[aa+126] = (colours.get('white'))
			led_colour[aa+183] = (colours.get('white'))
			led_colour[aa+184] = (colours.get('white'))
			led_colour[aa+185] = (colours.get('white'))
			led_colour[aa+242] = (colours.get('white'))
			led_colour[aa+243] = (colours.get('white'))
			led_colour[aa+244] = (colours.get('white'))
			led_colour[aa+245] = (colours.get('white'))
			led_colour[aa+246] = (colours.get('white'))
			led_colour[aa+304] = (colours.get('white'))
			led_colour[aa+241] = (colours.get('white'))
			led_colour[aa+247] = (colours.get('white'))

def b(spec):
	for b in range(len(led_colour1)):
		if b == spec:
			
			led_colour1[b+4] = (colours.get('purple'))
			led_colour1[b+63] = (colours.get('purple'))
			led_colour1[b+64] = (colours.get('purple'))			
			led_colour1[b+65] = (colours.get('purple'))
			led_colour1[b+122] = (colours.get('purple'))
			led_colour1[b+123] = (colours.get('purple'))
			led_colour1[b+124] = (colours.get('purple'))
			led_colour1[b+125] = (colours.get('purple'))
			led_colour1[b+126] = (colours.get('purple'))
			led_colour1[b+183] = (colours.get('purple'))
			led_colour1[b+184] = (colours.get('purple'))
			led_colour1[b+185] = (colours.get('purple'))
			led_colour1[b+242] = (colours.get('purple'))
			led_colour1[b+243] = (colours.get('purple'))
			led_colour1[b+244] = (colours.get('purple'))
			led_colour1[b+245] = (colours.get('purple'))
			led_colour1[b+246] = (colours.get('purple'))
			led_colour1[b+304] = (colours.get('purple'))
			led_colour1[b+241] = (colours.get('purple'))
			led_colour1[b+247] = (colours.get('purple'))
def bb(spec):
	for bb in range(len(led_colour)):
		if bb == spec:
			
			led_colour[bb+4] = (colours.get('purple'))
			led_colour[bb+63] = (colours.get('purple'))
			led_colour[bb+64] = (colours.get('purple'))			
			led_colour[bb+65] = (colours.get('purple'))
			led_colour[bb+122] = (colours.get('purple'))
			led_colour[bb+123] = (colours.get('purple'))
			led_colour[bb+124] = (colours.get('purple'))
			led_colour[bb+125] = (colours.get('purple'))
			led_colour[bb+126] = (colours.get('purple'))
			led_colour[bb+183] = (colours.get('purple'))
			led_colour[bb+184] = (colours.get('purple'))
			led_colour[bb+185] = (colours.get('purple'))
			led_colour[bb+242] = (colours.get('purple'))
			led_colour[bb+243] = (colours.get('purple'))
			led_colour[bb+244] = (colours.get('purple'))
			led_colour[bb+245] = (colours.get('purple'))
			led_colour[bb+246] = (colours.get('purple'))
			led_colour[bb+304] = (colours.get('purple'))
			led_colour[bb+241] = (colours.get('purple'))
			led_colour[bb+247] = (colours.get('purple'))
			
def c(spec):
	for c in range(len(led_colour1)):
		if c == spec:
			
			led_colour1[c+4] = (colours.get('pink'))
			led_colour1[c+63] = (colours.get('pink'))
			led_colour1[c+64] = (colours.get('pink'))			
			led_colour1[c+65] = (colours.get('pink'))
			led_colour1[c+122] = (colours.get('pink'))
			led_colour1[c+123] = (colours.get('pink'))
			led_colour1[c+124] = (colours.get('pink'))
			led_colour1[c+125] = (colours.get('pink'))
			led_colour1[c+126] = (colours.get('pink'))
			led_colour1[c+183] = (colours.get('pink'))
			led_colour1[c+184] = (colours.get('pink'))
			led_colour1[c+185] = (colours.get('pink'))
			led_colour1[c+242] = (colours.get('pink'))
			led_colour1[c+243] = (colours.get('pink'))
			led_colour1[c+244] = (colours.get('pink'))
			led_colour1[c+245] = (colours.get('pink'))
			led_colour1[c+246] = (colours.get('pink'))
			led_colour1[c+304] = (colours.get('pink'))
			led_colour1[c+241] = (colours.get('pink'))
			led_colour1[c+247] = (colours.get('pink'))			
def cc(spec):
	for cc in range(len(led_colour)):
		if cc == spec:
			
			led_colour[cc+4] = (colours.get('pink'))
			led_colour[cc+63] = (colours.get('pink'))
			led_colour[cc+64] = (colours.get('pink'))			
			led_colour[cc+65] = (colours.get('pink'))
			led_colour[cc+122] = (colours.get('pink'))
			led_colour[cc+123] = (colours.get('pink'))
			led_colour[cc+124] = (colours.get('pink'))
			led_colour[cc+125] = (colours.get('pink'))
			led_colour[cc+126] = (colours.get('pink'))
			led_colour[cc+183] = (colours.get('pink'))
			led_colour[cc+184] = (colours.get('pink'))
			led_colour[cc+185] = (colours.get('pink'))
			led_colour[cc+242] = (colours.get('pink'))
			led_colour[cc+243] = (colours.get('pink'))
			led_colour[cc+244] = (colours.get('pink'))
			led_colour[cc+245] = (colours.get('pink'))
			led_colour[cc+246] = (colours.get('pink'))
			led_colour[cc+304] = (colours.get('pink'))
			led_colour[cc+241] = (colours.get('pink'))
			led_colour[cc+247] = (colours.get('pink'))

def d(spec):
	for d in range(len(led_colour1)):
		if d == spec:
			
			led_colour1[d+4] = (colours.get('pink'))
			led_colour1[d+63] = (colours.get('pink'))
			led_colour1[d+64] = (colours.get('pink'))			
			led_colour1[d+65] = (colours.get('pink'))
			led_colour1[d+122] = (colours.get('pink'))
			led_colour1[d+123] = (colours.get('pink'))
			led_colour1[d+124] = (colours.get('pink'))
			led_colour1[d+125] = (colours.get('pink'))
			led_colour1[d+126] = (colours.get('pink'))
			led_colour1[d+183] = (colours.get('pink'))
			led_colour1[d+184] = (colours.get('pink'))
			led_colour1[d+185] = (colours.get('pink'))
			led_colour1[d+242] = (colours.get('pink'))
			led_colour1[d+243] = (colours.get('pink'))
			led_colour1[d+244] = (colours.get('pink'))
			led_colour1[d+245] = (colours.get('pink'))
			led_colour1[d+246] = (colours.get('pink'))
			led_colour1[d+304] = (colours.get('pink'))
			led_colour1[d+241] = (colours.get('pink'))
			led_colour1[d+247] = (colours.get('pink'))
def dd(spec):
	for dd in range(len(led_colour)):
		if dd == spec:
			
			led_colour[dd+4] = (colours.get('pink'))
			led_colour[dd+63] = (colours.get('pink'))
			led_colour[dd+64] = (colours.get('pink'))			
			led_colour[dd+65] = (colours.get('pink'))
			led_colour[dd+122] = (colours.get('pink'))
			led_colour[dd+123] = (colours.get('pink'))
			led_colour[dd+124] = (colours.get('pink'))
			led_colour[dd+125] = (colours.get('pink'))
			led_colour[dd+126] = (colours.get('pink'))
			led_colour[dd+183] = (colours.get('pink'))
			led_colour[dd+184] = (colours.get('pink'))
			led_colour[dd+185] = (colours.get('pink'))
			led_colour[dd+242] = (colours.get('pink'))
			led_colour[dd+243] = (colours.get('pink'))
			led_colour[dd+244] = (colours.get('pink'))
			led_colour[dd+245] = (colours.get('pink'))
			led_colour[dd+246] = (colours.get('pink'))
			led_colour[dd+304] = (colours.get('pink'))
			led_colour[dd+241] = (colours.get('pink'))
			led_colour[dd+247] = (colours.get('pink'))
			
def e(spec):
	for e in range(len(led_colour1)):
		if e == spec:
			
			led_colour1[e+4] = (colours.get('green'))
			led_colour1[e+63] = (colours.get('green'))
			led_colour1[e+64] = (colours.get('green'))			
			led_colour1[e+65] = (colours.get('green'))
			led_colour1[e+122] = (colours.get('green'))
			led_colour1[e+123] = (colours.get('green'))
			led_colour1[e+124] = (colours.get('green'))
			led_colour1[e+125] = (colours.get('green'))
			led_colour1[e+126] = (colours.get('green'))
			led_colour1[e+183] = (colours.get('green'))
			led_colour1[e+184] = (colours.get('green'))
			led_colour1[e+185] = (colours.get('green'))
			led_colour1[e+242] = (colours.get('green'))
			led_colour1[e+243] = (colours.get('green'))
			led_colour1[e+244] = (colours.get('green'))
			led_colour1[e+245] = (colours.get('green'))
			led_colour1[e+246] = (colours.get('green'))
			led_colour1[e+304] = (colours.get('green'))
			led_colour1[e+241] = (colours.get('green'))
			led_colour1[e+247] = (colours.get('green'))
def ee(spec):
	for ee in range(len(led_colour)):
		if ee == spec:
			
			led_colour[ee+4] = (colours.get('green'))
			led_colour[ee+63] = (colours.get('green'))
			led_colour[ee+64] = (colours.get('green'))			
			led_colour[ee+65] = (colours.get('green'))
			led_colour[ee+122] = (colours.get('green'))
			led_colour[ee+123] = (colours.get('green'))
			led_colour[ee+124] = (colours.get('green'))
			led_colour[ee+125] = (colours.get('green'))
			led_colour[ee+126] = (colours.get('green'))
			led_colour[ee+183] = (colours.get('green'))
			led_colour[ee+184] = (colours.get('green'))
			led_colour[ee+185] = (colours.get('green'))
			led_colour[ee+242] = (colours.get('green'))
			led_colour[ee+243] = (colours.get('green'))
			led_colour[ee+244] = (colours.get('green'))
			led_colour[ee+245] = (colours.get('green'))
			led_colour[ee+246] = (colours.get('green'))
			led_colour[ee+304] = (colours.get('green'))
			led_colour[ee+241] = (colours.get('green'))
			led_colour[ee+247] = (colours.get('green'))
			
def f(spec):
	for f in range(len(led_colour1)):
		if f == spec:
			
			led_colour1[f+4] = (colours.get('green'))
			led_colour1[f+63] = (colours.get('green'))
			led_colour1[f+64] = (colours.get('green'))			
			led_colour1[f+65] = (colours.get('green'))
			led_colour1[f+122] = (colours.get('green'))
			led_colour1[f+123] = (colours.get('green'))
			led_colour1[f+124] = (colours.get('green'))
			led_colour1[f+125] = (colours.get('green'))
			led_colour1[f+126] = (colours.get('green'))
			led_colour1[f+183] = (colours.get('green'))
			led_colour1[f+184] = (colours.get('green'))
			led_colour1[f+185] = (colours.get('green'))
			led_colour1[f+242] = (colours.get('green'))
			led_colour1[f+243] = (colours.get('green'))
			led_colour1[f+244] = (colours.get('green'))
			led_colour1[f+245] = (colours.get('green'))
			led_colour1[f+246] = (colours.get('green'))
			led_colour1[f+304] = (colours.get('green'))
			led_colour1[f+241] = (colours.get('green'))
			led_colour1[f+247] = (colours.get('green'))

def ff(spec):
	for ff in range(len(led_colour)):
		if ff == spec:
			
			led_colour[ff+4] = (colours.get('green'))
			led_colour[ff+63] = (colours.get('green'))
			led_colour[ff+64] = (colours.get('green'))			
			led_colour[ff+65] = (colours.get('green'))
			led_colour[ff+122] = (colours.get('green'))
			led_colour[ff+123] = (colours.get('green'))
			led_colour[ff+124] = (colours.get('green'))
			led_colour[ff+125] = (colours.get('green'))
			led_colour[ff+126] = (colours.get('green'))
			led_colour[ff+183] = (colours.get('green'))
			led_colour[ff+184] = (colours.get('green'))
			led_colour[ff+185] = (colours.get('green'))
			led_colour[ff+242] = (colours.get('green'))
			led_colour[ff+243] = (colours.get('green'))
			led_colour[ff+244] = (colours.get('green'))
			led_colour[ff+245] = (colours.get('green'))
			led_colour[ff+246] = (colours.get('green'))
			led_colour[ff+304] = (colours.get('green'))
			led_colour[ff+241] = (colours.get('green'))
			led_colour[ff+247] = (colours.get('green'))
			
Press = input("Press 1 to start animation:")
if Press == "1":	
	a(0)
	aa(0)
	b(9)
	bb(9)	
	c(18)
	cc(18)
	d(27)
	dd(27)
	e(36)
	ee(36)
	f(45)
	ff(45)
	client.put_pixels(led_colour)
	sleep(1)
	client.put_pixels(led_colour1)
	sleep(1)
	client.put_pixels(led_colour)
	sleep(1)
	client.put_pixels(led_colour1)
	sleep(1)
	client.put_pixels(led_colour)
	sleep(1)
	client.put_pixels(led_colour1)
	sleep(1)
	client.put_pixels(led_colour)
	sleep(1)
	client.put_pixels(led_colour1)
	sleep(1)
	client.put_pixels(led_colour)
	sleep(1)
	client.put_pixels(led_colour1)
	sleep(1)
	client.put_pixels(led_colour)
	sleep(1)
	client.put_pixels(led_colour1)
	sleep(1)
else:
    	print("replay and press 1")
sleep(1)

client.put_pixels(led_colour)
client.put_pixels(led_colour)
