# pip3 install pillow
# поменяем цвет одного пикселя

from PIL import Image

img = Image.open("white.jpg")

point = (0, 0)

color = img.getpixel(point)

r, g, b = color

r = 255 - r
g = 255 - g
b = 255 - b

color = (r, g, b)
img.putpixel(point, color)  # новый цвет пикселя

img.show() 
