import opc #opc library imported which allows to communicate with Fadecandy
import time # Time Library

client = opc.Client('localhost:7890')
sleep = time.sleep


Background = [(0,0,0)]*360  #Define the led colour for the background


    
def Background_Colour():# Define function for the background colour
    
    client.put_pixels(Background)
            
Background_Colour()
            
for a in range(0,60):   # Define "a" as a varible and select all leds from 0 to 60, complete single row.
    for a1 in range(0,6): #Define  "a1" as another varible each single column
        Background[a+60*a1] = (25,0,51)# Select list of leds, Complete single row multiply by 60.
        sleep(.01) # time delay
        Background_Colour()# background colour function
        
for b in range(0,60):                    
    for b2 in range(0,6):
        Background[b+60*b2] = (51,0,102)
        sleep(.01)
        Background_Colour()
                        
for c in range(0,60):
    for c2 in range(0,6):
        Background[c+60*c2] = (76,0,153)
        sleep(.01)
        Background_Colour()
        
for d in range(0,60):
    for d2 in range(0,6):
        Background[d+60*d2] = (102,0,204)
        sleep(.01)
        Background_Colour()
        
for e in range(0,60):
    for e2 in range(0,6):
        Background[e+60*e2] = (127,0,255)
        sleep(.01)
        Background_Colour()
        
for f in range(0,60):
    for f2 in range(0,6):
        Background[f+60*f2] = (153,51,255)
        sleep(.01)
        Background_Colour()
        
for g in range(0,60):
    for g2 in range(0,6):
        Background[g+60*g2] = (178,102,255)
        sleep(.01)
        Background_Colour()

for h in range(0,60):
    for h2 in range(0,6):
        Background[h+60*h2] = (204,153,255)
        sleep(.01)
        Background_Colour()
        
        

        
