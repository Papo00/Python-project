import opc
import time
import colorsys

client = opc.Client('localhost:7890')

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
while True:
    rainbow_movement()
