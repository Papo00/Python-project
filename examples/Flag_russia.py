import opc
import time
from time import sleep

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')

client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led<60: 
    for rows in range(2): #first 2 rows left to right
        leds[led+rows*60] = (255,255,255)
    for rows in range (4,6): #reverse last 2 rows right to left
        leds[59-led + rows*60] = (255,0,0)  
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

#the other way round from middle to right and left
led = 30  #because we need to start from the middle so we put 30
while led>=0: 
    for rows in range (2,4): #allocating the middle rows
        leds[led + rows*60] = (0,0,255) # from middle to right
        leds[59- led + rows*60] = (0,0,255)#from middle to left

    client.put_pixels(leds)
    time.sleep(.1)
    led = led - 1
