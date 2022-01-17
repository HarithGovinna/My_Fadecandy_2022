import opc
import time
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

temp = int(input("Enter your Body tempreture: "))
fever = int(input("how many days did you have fever : " ))
cough = int(input("how many days did you have dry cough: "))


if (temp>35 and fever>3 and cough>3):
    print("Your Body tempreature is " + str(temp))
    print("Days of Fever is :" + str(fever))
    print("Days of Dry cough is:" + str(cough))
    print("You are positive with Coroana Virus")

    for sign in range (22,23):
        for rows in range(3,4):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (23,24):
        for rows in range(4,5):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (24,25):
        for rows in range(5,6):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (25,26):
        for rows in range(4,5):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (26,27):
        for rows in range(3,4):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (27,28):
        for rows in range(2,3):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (28,29):
        for rows in range(1,2):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (29,30):
        for rows in range(0,1):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (32,33):
        for rows in range(3,4):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (33,34):
        for rows in range(4,5):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (34,35):
        for rows in range(5,6):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (35,36):
        for rows in range(4,5):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (36,37):
        for rows in range(3,4):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (37,38):
        for rows in range(2,3):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (38,39):
        for rows in range(1,2):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (39,40):
        for rows in range(0,1):
            leds[sign +rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    
else:
    print("Your Body tempreature is " +str(temp))
    print("Days of Fever is :" +str(fever))
    print("Days of Dry cough is:" + str(cough))
    print(" You are Negetive with Corona Virus")

    for sign in range (20,21):
        for rows in range(0,1):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (21,22):
        for rows in range(1,2):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (22,23):
        for rows in range(2,3):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (23,24):
        for rows in range(3,4):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (24,25):
        for rows in range(4,5):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (25,26):
        for rows in range(5,6):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (20,21):
        for rows in range(5,6):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (21,22):
        for rows in range (4,5):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (22,23):
        for rows in range(3,4):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (23,24):
        for rows in range(2,3):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (24,25):
        for rows in range(1,2):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (25,26):
        for rows in range(0,1):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (10,11):
        for rows in range(0,1):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (11,12):
        for rows in range(1,2):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (12,13):
        for rows in range(2,3):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (13,14):
        for rows in range(3,4):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (14,15):
        for rows in range(4,5):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (15,16):
        for rows in range(5,6):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (10,11):
        for rows in range(5,6):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (11,12):
        for rows in range (4,5):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (12,13):
        for rows in range(3,4):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (13,14):
        for rows in range(2,3):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

    for sign in range (14,15):
        for rows in range(1,2):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    for sign in range (15,16):
        for rows in range(0,1):
            leds[sign +rows*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)
