import opc
from time import sleep
import random

#leds =[(254,127,156),(0,255,0),(128,0,0)]
leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
'''
for item in enumerate(leds):
    sleep(1)
    print(item)
    client.put_pixels(leds)
'''


while True:
    for i in range(355):
        leds = [(255,255,255)]*360
        leds[i] = (0,0,255)
        leds[i+1] = (0,0,255)
        leds[i+2] = (0,0,255)
        leds[i+3] = (255,255,0)
        leds[i+4] = (255,255,0)
        leds[i+5] = (255,255,0)
        if i > 30:
            leds[i+30] = (0,0,255)
            leds[i+31] = (0,0,255)
            leds[i+32] = (0,0,255)
            leds[i+33] = (255,255,0)
            leds[i+34] = (255,255,0)
            leds[i+35] = (255,255,0)
               
           
        
        if leds == 255:
            leds=0
        
        client.put_pixels(leds)
        sleep(.1)
    
        
   
   

    
