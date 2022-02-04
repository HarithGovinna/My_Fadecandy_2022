import opc, time

led_frame = [(255,255,255)]*360
client = opc.Client('localhost:7890')

while True:
    led = 0
    while led<60:
        for rows in range(6):
            led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.02), 205 * ((led / 30)- 0.03))
            led_frame[59-led + rows*60] = led_color
        time.sleep(.1)
        client.put_pixels(led_frame)
        led = led + 1 #or reverse if you want


    led = 0
    while led<60:
        for rows in range(6):
            led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.1), 205 * ((led / 30)- 0.2))
            led_frame[led + rows*60] = led_color
        time.sleep(.1)
        client.put_pixels(led_frame)
        led = led + 1 #or reverse if you want


# while True:
#     led = 0
#     while led < 60:
#         for led in range (360):
#             led_color = (106 * ((led / 5) - 0.01), 90 * ((led / 5) - 0.1), 205 * ((led / 5)- 0.2))
#             for rows in range (6):
#                 led_frame[led ] = led_color
#                 led_frame[59- led ] = led_color
#                 client.put_pixels(led_frame)
#                 time.sleep(0.1)
#                 led =+ 1
