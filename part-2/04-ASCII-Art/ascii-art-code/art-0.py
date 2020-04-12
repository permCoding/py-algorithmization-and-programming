# pip3 install pillow
# узнаем компоненты цвета пикселя

from PIL import Image

img = Image.open("white.jpg")

point = (0, 0)

r, g, b = img.getpixel(point)

print(r, g, b)

