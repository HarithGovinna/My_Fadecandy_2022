import opc, time

client = opc.Client('localhost:7890')

leds1 =[(0,0,0)]*360
leds2 =[(0,0,0)]*360

flag_positions1 = [[0,1,2,3,0,5,0,0,255], [3,4,5,6,0,5,255,255,0], [6,7,8,9,0,5,255,0,0], [9,10,11,12,0,5,255,255,255], [12,13,14,15,0,5,255,165,0], [15,16,17,18,0,1,0,0,255], [15,16,17,18,1,2,255,255,0], [15,16,17,18,2,3,255,0,0], [15,16,17,18,3,4,255,255,255], [15,16,17,18,4,5,255,165,0]]
for i, item in enumerate(flag_positions1):
    for one in range(item[0], item[3]):
        for row in range(item[4], item[5]):
            leds1[one+row*60] = (item[6], item[7], item[8])
        client.put_pixels(leds1)
        time.sleep(0.3)
        
flag_positions2 = [[57,58,59,60,0,5,0,0,255], [54,55,56,57,0,5,255,255,0], [51,52,53,54,0,5,255,0,0], [48,49,50,51,0,5,255,255,255], [45,46,47,48,0,5,255,165,0], [42,43,44,45,0,1,0,0,255], [42,43,44,45,1,2,255,255,0], [42,43,44,45,2,3,255,0,0], [42,43,44,45,3,4,255,255,255], [42,43,44,45,4,5,255,165,0]]
for j, item in enumerate(flag_positions2):
    for one in range(item[0], item[3]):
        for row in range(item[4], item[5]):
            leds2[one+row*60] = (item[6], item[7], item[8])
        client.put_pixels(leds2)
        time.sleep(0.3)

while True:
	client.put_pixels(leds1)
	time.sleep(0.8)
	client.put_pixels(leds2)
	time.sleep(0.8)
	
    


