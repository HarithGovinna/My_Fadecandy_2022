import opc
from time import sleep
import random


leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


for one in range (6,7):   #1 st part
    for rows in range(0,1):
        leds[one+rows *60] = (254,127,156)  #pink
client.put_pixels(leds)
sleep(.1)
'''
for one in range (17,18):
    for rows  in range(0,1):
        leds[one+rows *60] = (254,127,156)
client.put_pixels(leds)
sleep(.1)

for one in range (29,30):
    for rows  in range(0,1):
        leds[one+rows *60] = (254,127,156)
client.put_pixels(leds)
sleep(.1)

for one in range (41,42):
    for rone in range(0,1):
        leds[one+rone*60] = (254,127,156)
client.put_pixels(leds)
sleep(.1)

for one in range (53,54):
    for rows in range(0,1):
        leds[one+rows *60] = (254,127,156)
client.put_pixels(leds)
sleep(.1)



for one in range (5,8):   # 2 nd part
    for rows in range(1,2):
        leds[one+rows *60] = (0,255,0)  #green
client.put_pixels(leds)
sleep(.1)

for one in range (16,19):   
    for rone in range(1,2):
        leds[one+rone*60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)

for one in range (28,31):   
    for rows  in range(1,2):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)

for one in range (40,43):   
    for rows  in range(1,2):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)

for one in range (52,55):   
    for rows  in range(1,2):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)


for one in range (4,9):    #3 rd part
    for rows  in range(2,3):
        leds[one+rows *60] = (128,0,0)  #maroon
client.put_pixels(leds)
sleep(.1)

for one in range (15,20):
    for rows  in range(2,3):
        leds[one+rows *60] = (128,0,0)
client.put_pixels(leds)
sleep(.1)

for one in range (27,32):
    for rows  in range(2,3):
        leds[one+rows *60] = (128,0,0)
client.put_pixels(leds)
sleep(.1)

for one in range (39,44):
    for rows  in range(2,3):
        leds[one+rows *60] = (128,0,0)
client.put_pixels(leds)
sleep(.1)

for one in range (51,56):
    for rows  in range(2,3):
        leds[one+rows *60] = (128,0,0)
client.put_pixels(leds)
sleep(.1)




for one in range (3,10):     #4 th part
    for rows  in range(3,4):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)

for one in range (14,21):
    for rows  in range(3,4):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)

for one in range (26,33):
    for rows  in range(3,4):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)

for one in range (38,45):
    for rows  in range(3,4):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)

for one in range (50,57):
    for rows  in range(3,4):
        leds[one+rows *60] = (0,255,0)
client.put_pixels(leds)
sleep(.1)




for one in range (2,11):    #Last part 5
    for rows  in range(4,5):
        leds[one+rows *60] = (255,140,0)  #dark orange
client.put_pixels(leds)
sleep(.1)

for one in range (13,22):
    for rows  in range(4,5):
        leds[one+rows *60] = (255,140,0)
client.put_pixels(leds)
sleep(.1)

for one in range (25,34):
    for rows in range(4,5):
        leds[one+rows *60] = (255,140,0)
client.put_pixels(leds)
sleep(.1)

for one in range (37,46):
    for rows  in range(4,5):
        leds[one+rows *60] = (255,140,0)
client.put_pixels(leds)
sleep(.1)

for one in range (49,58):
    for rows  in range(4,5):
        leds[one+rows *60] = (255,140,0)
client.put_pixels(leds)
sleep(.1)


for one in range (5,8):   #Leg part
    for rows  in range(5,6):
        leds[one+rows *60] = (178,34,34)   #Firebrick
client.put_pixels(leds)
sleep(.1)


for one in range (16,19):  
    for rows  in range(5,6):
        leds[one+rows *60] = (178,34,34)
client.put_pixels(leds)
sleep(.1)

for one in range (28,31):  
    for rows  in range(5,6):
        leds[one+rows *60] = (178,34,34)
client.put_pixels(leds)
sleep(.1)

for one in range (40,43):  
    for rows  in range(5,6):
        leds[one+rows *60] = (178,34,34)
client.put_pixels(leds)
sleep(.1)

for one in range (52,55):  
    for rows  in range(5,6):
        leds[one+rows *60] = (178,34,34)
client.put_pixels(leds)
sleep(.1)

'''


