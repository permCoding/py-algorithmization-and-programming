import turtle
from init import *


w = turtle.Screen()
w.bgcolor(bgcolor)
height = w.window_height()
width = w.window_width()

alex = turtle.Turtle()
alex.shape(names[pos_name])

alex.color(fgcolor)
alex.pensize(pensize)

alex.speed(0)
alex.penup()
alex.setpos(-199, +199)
alex.setpos(-width//2+10, +height//2-10)

# alex.setx(-200)

alex.speed(speed)

step = 150
square(alex, step)

w.mainloop()
