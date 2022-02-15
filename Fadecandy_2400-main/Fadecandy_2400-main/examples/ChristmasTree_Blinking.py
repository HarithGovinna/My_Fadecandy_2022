import opc, time

leds =[(255,255,255)]*360
leds1 =[(255,255,255)]*360
leds2 =[(255,255,255)]*360
leds3 =[(255,255,255)]*360
leds4 =[(255,255,255)]*360
leds5 =[(255,255,255)]*360

client = opc.Client('localhost:7890')
        
Tree_positions1 = [[6,7,0,1], [17,18,0,1], [29,30,0,1], [41,42,0,1], [53,54,0,1]]
for i, item in enumerate(Tree_positions1):
    for one in range(item[0], item[1]):
        for row in range(item[2], item[3]):
            leds[one+row*60] = (255,0,0)         #Red
            leds1[one+row*60] = (0,255,0)        #Green
            leds2[one+row*60] = (148,0,211)      #Violet
            leds3[one+row*60] = (255, 255, 0)    #Yellow
            leds4[one+row*60] = (0,0,255)        #Blue
            leds5[one+row*60] = (254,127,156)    #Pink
            

        
Tree_positions2 = [[5,6,7,8,1,2], [16,17,18,19,1,2], [28,29,30,31,1,2], [40,41,42,43,1,2], [52,53,54,55,1,2]]
for i, item in enumerate(Tree_positions2):
    for one in range(item[0], item[3]):
        for row in range(item[4], item[5]):
            leds[one+row*60] = (255,0,0)         #Red
            leds1[one+row*60] = (0,255,0)       #Green
            leds2[one+row*60] = (255,0,255)     #Violet
            leds3[one+row*60] = (255, 255, 0)    #Yellow
            leds4[one+row*60] = (0,0,255)        #Blue
            leds5[one+row*60] = (254,127,156)    #Pink
            

Tree_positions3 = [[4,5,6,7,8,9,2,3], [15,16,17,18,19,20,2,3], [27,28,29,30,31,32,2,3], [39,40,41,42,43,44,2,3], [51,52,53,54,55,56,2,3]]
for i, item in enumerate(Tree_positions3):
    for one in range(item[0], item[5]):
        for row in range(item[6], item[7]):
            leds[one+row*60] = (255,0,0)
            leds1[one+row*60] = (0,255,0)
            leds2[one+row*60] = (255,0,255)
            leds3[one+row*60] = (255, 255, 0)    #Yellow
            leds4[one+row*60] = (0,0,255)        #Blue
            leds5[one+row*60] = (254,127,156)    #Pink

Tree_positions4 = [[3,4,5,6,7,8,9,10,3,4], [14,15,16,17,18,19,20,21,3,4], [26,27,28,29,30,31,32,33,3,4], [38,39,40,41,42,43,44,45,3,4], [50,51,52,53,54,55,56,57,3,4]]
for i, item in enumerate(Tree_positions4):
    for one in range(item[0], item[7]):
        for row in range(item[8], item[9]):
            leds[one+row*60] = (255,0,0)
            leds1[one+row*60] = (0,255,0)
            leds2[one+row*60] = (255,0,255)
            leds3[one+row*60] = (255, 255, 0)    #Yellow
            leds4[one+row*60] = (0,0,255)        #Blue
            leds5[one+row*60] = (254,127,156)    #Pink

Tree_positions5 = [[2,3,4,5,6,7,8,9,10,11,4,5], [13,14,15,16,17,18,19,20,21,22,4,5], [25,26,27,28,29,30,31,32,33,34,4,5], [37,38,39,40,41,42,43,44,45,46,4,5], [49,50,51,52,53,54,55,56,57,58,4,5]]
for i, item in enumerate(Tree_positions5):
    for one in range(item[0], item[9]):
        for row in range(item[10], item[11]):
            leds[one+row*60] = (255,0,0)
            leds1[one+row*60] = (0,255,0)
            leds2[one+row*60] = (255,0,255)
            leds3[one+row*60] = (255, 255, 0)    #Yellow
            leds4[one+row*60] = (0,0,255)        #Blue
            leds5[one+row*60] = (254,127,156)    #Pink

Tree_positions6 = [[5,6,7,8,5,6], [16,17,18,19,5,6], [28,29,30,31,5,6], [40,41,42,43,5,6], [52,53,54,55,5,6]]
for i, item in enumerate(Tree_positions6):
    for one in range(item[0], item[3]):
        for row in range(item[4], item[5]):
            leds[one+row*60] = (255,0,0)
            leds1[one+row*60] = (0,255,0)
            leds2[one+row*60] = (255,0,255)
            leds3[one+row*60] = (255, 255, 0)    #Yellow
            leds4[one+row*60] = (0,0,255)        #Blue
            leds5[one+row*60] = (254,127,156)    #Pink

while True:
    client.put_pixels(leds)
    time.sleep(0.4)
    client.put_pixels(leds1)
    time.sleep(0.4)
    client.put_pixels(leds2)
    time.sleep(0.4)
    client.put_pixels(leds3)
    time.sleep(0.4)
    client.put_pixels(leds4)
    time.sleep(0.4)
    client.put_pixels(leds5)
    time.sleep(0.4)
