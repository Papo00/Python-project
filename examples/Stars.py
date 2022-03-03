import opc
from time import sleep
import colorsys

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

#Assigning pixels for star

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

