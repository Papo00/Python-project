import opc
import time
from time import sleep

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')

client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led<15:
    for rows in range(4):
       leds[led+rows*60] = (0,0,255)
       client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
time.sleep(0.4)

for q in range(15,60):
    leds[q] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for w in range(75,120):
    leds[w] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)
for e in range(135,180):
    leds[e] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for r in range(195,240):
    leds[r] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)
for t in range(240,300):
    leds[t] = (255,0,0)
    time.sleep(0.1)
    client.put_pixels(leds)
for y in range(300,360):
    leds[y] = (255,255,255)
    time.sleep(0.1)
    client.put_pixels(leds)
    
    













