

import opc
import time

import colorsys
from time import sleep
from random import seed
from random import randint

led =[(250,0,0)]*360  
    
led_colour = [(250,0,0)]*360 
client = opc.Client('localhost:7890')


for i in range (0,20,2):
        for x in range(0,6):
            led_colour[i*10+1*x] = (140,40,140)
fade_amount =5                    
while True:
        for led in enumerate(led_colour): 
                                        
            r,g,b = led[1]              
            r = r+fade_amount
            g = g+fade_amount
            b = b+fade_amount

            new_colour = (g,r,b)        
            led_colour[led[0]] = new_colour   
                
            if r >=255 or r <= 0:           
                fade_amount = -fade_amount  
                
        client.put_pixels(led_colour)         
        sleep(.2)  
