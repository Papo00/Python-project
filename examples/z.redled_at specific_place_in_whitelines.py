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



