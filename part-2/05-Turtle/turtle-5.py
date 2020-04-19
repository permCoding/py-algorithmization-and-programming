import turtle
from init import *


w = turtle.Screen()
w.bgcolor(bgcolor)
height = w.window_height()
width = w.window_width()

alex = turtle.Turtle()
alex.hideturtle()
alex.shape(names[pos_name])
alex.color(fgcolor)
alex.pensize(pensize)

pos_x, pos_y = -width // 2 + 10, +height // 2 - 10
change_pos(alex, pos_x, pos_y)
alex.showturtle()

step = 150
square(alex, step)

x, y = alex.pos()

print(x, y)

w.mainloop()
