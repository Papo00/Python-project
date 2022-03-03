import opc
import time
import random

leds = [(0,0,0)]*360 #white leds

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

leds[59] = (255,0,0) #pixel 59 red
leds[59+60] = (0,255,0) #pixel 119 green
leds[119+60] = (0,0,255) #pixel 179 blue
leds[179+60] = (245,0,222) #pixel 239 pink
leds[239+60] = (235,235,35) #pixel 299 yellow
leds[299+60] = (90,200,150) #pixel 259 light green
time.sleep(0.3) 
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(0,60):
    leds[led] = (90,200,150)
    time.sleep(.1)
    client.put_pixels(leds)
for led in range(60,120):
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)
for led in range(120,180):
    leds[led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)
for led in range(180,240):
    leds[led] = (0,0,255)
    time.sleep(.1)
    client.put_pixels(leds)
for led in range(240,300):
    leds[led] = (245,0,222)
    time.sleep(.1)
    client.put_pixels(leds)
for led in range(300,360):
    leds[led] = (235,235,35)
    time.sleep(.1)
    client.put_pixels(leds)
    
    
