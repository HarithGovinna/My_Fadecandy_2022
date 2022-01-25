import opc
from time import sleep
import random


leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for one in range (0,3):   #1 st part
    for column in range(0,5):
        leds[one+column *60] = (0,0,255)  #blue
client.put_pixels(leds)
sleep(.1)

for one in range (3,6):   #2 st part
    for column in range(0,5):
        leds[one+column *60] = (255,255,0)  #yellow
client.put_pixels(leds)
sleep(.1)

for one in range (6,9):   #3 st part
    for column in range(0,5):
        leds[one+column *60] = (255,0,0)  #red
client.put_pixels(leds)
sleep(.1)

for one in range (9,12):   #4 st part
    for column in range(0,5):
        leds[one+column *60] = (255,255,255)  #white
client.put_pixels(leds)
sleep(.1)

for one in range (12,15):   #5 st part
    for column in range(0,5):
        leds[one+column *60] = (255,165,0)  #orange
client.put_pixels(leds)
sleep(.1)


for one in range (15,18):  
    for rows in range(0,1):
        leds[one+rows*60] = (0,0,255)  #blue
client.put_pixels(leds)
sleep(.1)

for one in range (15,18): 
    for rows in range(1,2):
        leds[one+rows*60] = (255,255,0)  #yellow
client.put_pixels(leds)
sleep(.1)

for one in range (15,18):   
    for rows in range(2,3):
        leds[one+rows*60] = (255,0,0) #red
client.put_pixels(leds)
sleep(.1)

for one in range (15,18):   
    for rows in range(3,4):
        leds[one+rows*60] = (255,255,255) #white
client.put_pixels(leds)
sleep(.1)

for one in range (15,18):   
    for rows in range(4,5):
        leds[one+rows*60] = (255,165,0) #orange
client.put_pixels(leds)
sleep(.1)

for one in range (21,22):   
    for rows in range(0,1):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (22,23):   
    for rows in range(1,2):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (23,24):   
    for rows in range(2,3):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (24,25):   
    for rows in range(3,4):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (25,26):   
    for rows in range(4,5):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (26,27):   
    for rows in range(3,4):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (27,28):   
    for rows in range(2,3):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (28,29):   
    for rows in range(1,2):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (29,30):   
    for rows in range(0,1):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (32,37):   
    for rows in range(0,1):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (32,37):   
    for rows in range(2,3):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (32,37):   
    for rows in range(4,5):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (32,33):   
    for rows in range(1,2):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)

for one in range (36,37):   
    for rows in range(3,4):
        leds[one+rows*60] = (254,127,156) #pink
client.put_pixels(leds)
sleep(.1)
