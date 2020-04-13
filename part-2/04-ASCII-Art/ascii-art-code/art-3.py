# pip3 install pillow
# инвертируем цвет у нескольких пикселей

from PIL import Image


def get_color_invert(color):
    '''
    инвертировать цвет пикселя
    '''
    r, g, b = color
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return (r, g, b)


# img = Image.open("white.jpg")
img = Image.open("белка.jpg")
width, height = img.size

for y in range(height):
    for x in range(width):
        if y > x: # левый нижний
            color = img.getpixel((x, y))
            img.putpixel((x, y), get_color_invert(color))

img.show()
