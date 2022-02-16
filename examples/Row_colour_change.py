import opc
import time
from time import sleep


client = opc.Client('localhost:7890')
leds=[(255,255,255)]*360 #white leds background

#First row
def lines():
     
     for led in range(0, 60):  #left to right first row
          leds[led]=(255,55,5) #orange led
          client.put_pixels(leds)#to place using put pixels method
          sleep(0.01) #delay

#second row
     for led in range(119, 59,-1): #right to left second row
              leds[led]=(255,55,5) #orange led
              client.put_pixels(leds) #to place using put pixels method
              sleep(0.01) #delay
     for led in range(60,120): #left to right second row
              leds[led]=(0,0,255) #blue led
              client.put_pixels(leds) #to place using put pixels method
              sleep (0.01) #delay
              
#third row           
     for led in range(179,119,-1): #right to left third row
              leds[led]=(0,0,255) #blue led
              client.put_pixels(leds) #to place using put pixels method
              sleep (0.01)#delay
     for led in range(120,180): #left to right third row
              leds[led]=(245,0,245) #pink led
              client.put_pixels(leds) #to place using put pixels method
              sleep(0.01) #delay
              
#forth row           
     for led in range(239,179,-1): #right to left fourth row
              leds[led]=(245,0,245) #pink led
              client.put_pixels(leds) #to place using put pixels method
              sleep(0.01) #delay
     for led in range(180,240): #left to right fourth row
              leds[led]= (235,235,35) #yellow led
              client.put_pixels(leds) #to place using put pixels method
              sleep(0.01) #delay
              
#fifth row           
     for led in range(299,239,-1): #right to left fifth row
             leds[led]=(235,235,35) #yellow led
             client.put_pixels(leds) #to place using put pixels method
             sleep(0.01) #delay
     for led in range(240,300): #left to right fifth row
             leds[led]=(255,0,0) #red led
             client.put_pixels(leds) #to place using put pixels method
             sleep(0.01) #delay
             
#sixth row          
     for led in range(359,299,-1): #right to left sixth row
             leds[led]=(255,0,0) #red led
             client.put_pixels(leds) #to place using put pixels method
             sleep(0.01) #delay
     for led in range(300,360): #left to right sixth row
             leds[led]=(0,255,0) #green led
             client.put_pixels(leds)#to place using put pixels method
             sleep(0.01) #delay
lines()
led = 0
while led<30:
    for rows in range (6):
        leds[led + rows*60] = (90,200,150) #scroll from right
        #same time to meet in the middle
        leds[59- led + rows*60] = (90,200,150)#reverse scroll from left
        
    client.put_pixels(leds)
    time.sleep(.1) #delay
    led = led + 1


#from middle to right and left
led = 30  #To start from the middle
while led>=0: 
    for rows in range (6):
        leds[led + rows*60] = (230,0,100) #scroll from middle to right
        #same time to start from middle
        leds[59- led + rows*60] = (230,0,100)#reverse scroll from middle to left

    client.put_pixels(leds)
    time.sleep(.1) #delay
    led = led - 1
