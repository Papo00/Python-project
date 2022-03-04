import opc
from time import sleep
import time
import random
import colorsys
from random import seed
from random import randint

client = opc.Client('localhost:7890')
leds=[(255,255,255)]*360 #white leds background

while True:
    print ("Welcome to the menu, which animation would you like to see: \n\t a.2 rows colour change \n\t b.Reach last pixel\n\t c.Rainbow \n\t d.Star \n\t e.Netherland flag \n\t f.American flag \n\t g.italian flag \n\t h.Fade animation \n")
    value = input ("please choose from the list:")
        
    if value == 'a':
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
                    led = led -1
    elif value == "b":
            leds = [(0,0,0)]*360 #white leds
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
                time.sleep(0.01)
                client.put_pixels(leds)
            for led in range(60,120):
                leds[led] = (255,0,0)
                time.sleep(0.01)
                client.put_pixels(leds)
            for led in range(120,180):
                leds[led] = (0,255,0)
                time.sleep(0.01)
                client.put_pixels(leds)
            for led in range(180,240):
                leds[led] = (0,0,255)
                time.sleep(0.01)
                client.put_pixels(leds)
            for led in range(240,300):
                leds[led] = (245,0,222)
                time.sleep(0.01)
                client.put_pixels(leds)
            for led in range(300,360):
                leds[led] = (235,235,35)
                time.sleep(0.01)
                client.put_pixels(leds)
                
    elif value == "c":
        
        s=1
        v=1
        def rainbow_movement():
            rainbow=[(0, 0, 0)]*360
            for i in range(60):
                for x in range(0,360,60):
                    r, g, b = colorsys.hsv_to_rgb(i/30 ,s ,v )

                    r = r * 255
                    g = g * 255
                    b = b * 255
                    rainbow[i+x] = (r,g,b)
                    client.put_pixels(rainbow)
                    time.sleep(0.01)

        rainbow_movement()
        
    elif value == "d":
        leds = [(0,0,0)]*360
        star_left = [30,
                  88,89,90,
                  143,144,145,146,147,148,149,150, #for left side of the star
                  206,207,208,209,210,
                  265,266,267,268,
                  324,325]

        star_right = [31,
                  91,92,93,
                  151,152,153,154,155,156,157,158, #for right side of the star
                  211,212,213,214,215,
                  273,274,275,276,
                  336,337]

        s = 1 #maximum colour
        v = 1 #maximum brightness


        def left():
                for hue in star_left:
                    rgb_fractional = colorsys.hsv_to_rgb(hue*2/360.0, s, v) 
                    r_float = rgb_fractional[0]*255
                    g_float = rgb_fractional[1]*255
                    b_float = rgb_fractional[2]*255
                    rgb = (r_float ,g_float ,b_float) #tuple with correct values
                    leds[hue]=rgb
                    client.put_pixels(leds)  
                    sleep(0.1) #delay

        def right():
                for i in star_right:
                    rgb_fractional = colorsys.hsv_to_rgb(i*2/360.0, s, v)
                    r_float = rgb_fractional[0]*255
                    g_float = rgb_fractional[1]*255
                    b_float = rgb_fractional[2]*255
                    rgb = (r_float ,g_float ,b_float)
                    leds[i]=rgb
                    client.put_pixels(leds)
                    sleep(0.1)


                left()

        right()
    elif value == "e":
            leds=[(0,0,0)]*360
            led = 0
            while led<60:
                for rows in range(2): #first 2 rows left to right
                    leds[led+rows*60] = (255,0,0)
                for rows in range (4,6): #reverse last 2 rows right to left
                    leds[59-led + rows*60] = (0,0,255)  
                client.put_pixels(leds)
                time.sleep(.1)
                led = led + 1

            #from middle to right and left
            led = 30  #starting from the middle so we put 30
            while led>=0: 
                for rows in range (2,4):     #allocating the middle row
                    leds[led + rows*60] = (255,255,255) # from middle to right
                    leds[59- led + rows*60] = (255,255,255)#from middle to left

                client.put_pixels(leds)
                time.sleep(.1)
                led = led - 1
    elif value == "f":
        leds=[(0,0,0)]*360
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
    elif value == "g":
        leds=[(255,255,255)]*360
        led = 0
        while led<20:
            for rows in range(6):
                leds[led+rows*60] = (0,255,0)
                leds[59-led+rows*60] = (255,0,0)
                client.put_pixels(leds)
            time.sleep(.1)
            led = led + 1
    elif value == "h":
        led =[(250,0,0)]*360  
        led_colour = [(250,0,0)]*360 
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

        
