# pip3 install pillow
# сделать градиент

from PIL import Image


img = Image.open("white.jpg")
width, height = img.size

for y in range(height):
    for x in range(width):
        r = y; g = y; b = y
        img.putpixel((x, y), (r, g, b))

img.show()