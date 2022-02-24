import opc
import time

client = opc.Client('localhost:7890')
sleep = time.sleep

leds = [(0,255,0)]*360
leds1 = [(20,255,200)]*360
leds2 = [(240,40,0)]*30
leds3 = [(30,20,0)]*350
leds4 = [(0,40,0)]*260
leds5 = [(20,0,25)]*360
leds6 = [(0,30,65)]*360
leds7 = [(60,0,25)]*360
leds8 = [(255,60,55)]*360
leds9 = [(0,70,255)]*120
leds10 = [(50,0,25)]*130
leds11 = [(80,0,0)]*140
leds12 = [(60,40,0)]*150
leds13 = [(10,100,0)]*170
leds14 = [(100,10,255)]*180
leds15 = [(90,40,0)]*220
leds16 = [(255,20,0)]*250
leds17 = [(20,0,55)]*280
leds18 = [(20,0,55)]*300
leds19 = [(90,30,255)]*340
leds20 = [(100,0,25)]*360





client.put_pixels(leds)
sleep(0.2)

client.put_pixels(leds)
sleep(0.02)

for x in range(0,360):

            client.put_pixels(leds1)
            sleep(0.1)

            client.put_pixels(leds2)
            sleep(0.1)

            client.put_pixels(leds3)
            sleep(0.1)

            client.put_pixels(leds4)
            sleep(0.1)

            client.put_pixels(leds5)
            sleep(0.1)

            client.put_pixels(leds6)
            sleep(0.1)

            client.put_pixels(leds7)
            sleep(0.1)

            client.put_pixels(leds8)
            sleep(0.1)

            client.put_pixels(leds9)
            sleep(0.1)

            client.put_pixels(leds10)
            sleep(0.1)

            client.put_pixels(leds11)
            sleep(0.1)

            client.put_pixels(leds12)
            sleep(0.1)

            client.put_pixels(leds13)
            sleep(0.1)

            client.put_pixels(leds14)
            sleep(0.1)

            client.put_pixels(leds15)
            sleep(0.1)

            client.put_pixels(leds16)
            sleep(0.1)

            client.put_pixels(leds17)
            sleep(0.1)

            client.put_pixels(leds18)
            sleep(0.1)

            client.put_pixels(leds19)
            sleep(0.1)

            client.put_pixels(leds20)
            sleep(0.1)



            
