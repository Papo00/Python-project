import opc
import time
from time import sleep

leds=[(255,255,255)]*360
client = opc.Client('localhost:7890')

client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led<20:
    for rows in range(6):
        leds[led+rows*60] = (0,255,0)
        leds[59-led+rows*60] = (255,0,0)
        client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
