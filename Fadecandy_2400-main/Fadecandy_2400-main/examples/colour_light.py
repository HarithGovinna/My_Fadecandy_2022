import opc, time

numLEDs = 512
client = opc.Client('localhost:7890')

red = [(255, 0, 17)] * numLEDs
green = [(0, 255, 0)] * numLEDs
yellow = [(255, 140, 0)]* numLEDs

while True:
    client.put_pixels(green)
    time.sleep(0.4) 
    client.put_pixels(red)
    time.sleep(0.4)
    client.put_pixels(yellow)
    time.sleep(0.4)
    
		