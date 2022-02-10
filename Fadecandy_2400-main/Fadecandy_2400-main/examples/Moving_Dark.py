import opc
import time

leds = [(0,0,0)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

while True:
    led = 0
    while led<30: #scroll all rows at the same time
        led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.1), 205 * ((led / 30)- 0.2))
        for rows in range(6): #first three rows left to right
            leds[29-led + rows*60] = led_color
        for rows in range(6):
            leds[30+led + rows* 60] = led_color
        client.put_pixels(leds)
        time.sleep(.1)
        led = led + 1

    led = 0
    while led<=30:
        for rows in range(6):
            led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.1), 205 * ((led / 30)- 0.2))
            leds[led + rows*60] = led_color
            leds[59-led + rows*60] = led_color
        time.sleep(.1)
        client.put_pixels(leds)
        led = led + 1 #or reverse if you want

    led = 0
    while led<30: #scroll all rows at the same time
        led_color2 = (255 * ((led / 30) - 0.01), 140 * ((led / 30) - 0.1), 0)
        for rows in range(6): #first three rows left to right
            leds[29-led + rows*60] = led_color2
        for rows in range(6):
            leds[30+led + rows* 60] = led_color2
        client.put_pixels(leds)
        time.sleep(.1)
        led = led + 1

    led = 0
    while led<=30:
        for rows in range(6):
            led_color2 = (255 * ((led / 30) - 0.01), 140 * ((led / 30) - 0.1), 0)
            leds[led + rows*60] = led_color2
            leds[59-led + rows*60] = led_color2
        time.sleep(.1)
        client.put_pixels(leds)
        led = led + 1 #or reverse if you want
