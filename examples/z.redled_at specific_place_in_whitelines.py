import opc
import time
import random

leds = [(255,255,255)]*360 #red,green,blue so you get a while one

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

leds[59] = (255,0,0) #to make pixel 10 red
time.sleep(0.1) #delay
client.put_pixels(leds)#to place it using put pixel method
client.put_pixels(leds)

leds[59+60] = (0,255,0) #to make pixel 10 red
time.sleep(0.1) #delay
client.put_pixels(leds)#to place it using put pixel method
client.put_pixels(leds)

leds[119+60] = (0,0,255) #to make pixel 10 red
time.sleep(0.1) #delay
client.put_pixels(leds)#to place it using put pixel method
client.put_pixels(leds)

leds[179+60] = (245,0,222) #to make pixel 10 red
time.sleep(0.1) #delay
client.put_pixels(leds)#to place it using put pixel method
client.put_pixels(leds)

leds[239+60] = (235,235,35) #to make pixel 10 red
time.sleep(0.1) #delay
client.put_pixels(leds)#to place it using put pixel method
client.put_pixels(leds)

leds[299+60] = (90,200,150) #to make pixel 10 red
time.sleep(0.1) #delay
client.put_pixels(leds)#to place it using put pixel method
client.put_pixels(leds)



