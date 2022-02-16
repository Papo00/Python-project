import opc
import time
from time import sleep


client = opc.Client('localhost:7890')
leds=[(255,255,255)]*360

for led in range(0, 60):
          leds[led]=(255,55,5) 
          client.put_pixels(leds)
          sleep(0.01) 
for led in range(60,120):
              leds[led]=(0,0,255)
              client.put_pixels(leds)
              sleep (0.01)
for led in range(120,180):
              leds[led]=(245,0,245)
              client.put_pixels(leds)
              sleep(0.01)
for led in range(180,240):
              leds[led]= (235,235,35)
              client.put_pixels(leds)
              sleep(0.01)
for led in range(240,300):
             leds[led]=(255,0,0)
             client.put_pixels(leds)
             sleep(0.01)
for led in range(300,360):
             leds[led]=(0,255,0)
             client.put_pixels(leds)
             sleep(0.01)
