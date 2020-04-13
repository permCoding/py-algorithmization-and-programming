# pip3 install pillow
# узнаем компоненты цвета пикселя

from PIL import Image

img = Image.open("white.jpg")

point = (0, 0)

color = img.getpixel(point)

r, g, b = color

print(r, g, b)

