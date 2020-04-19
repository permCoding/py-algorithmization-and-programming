import turtle
from init import *


w = turtle.Screen()
w.bgcolor(bgcolor)

alex = turtle.Turtle()
alex.shape(names[pos_name])

alex.color(fgcolor)
alex.speed(speed)
alex.pensize(pensize)

step = 150

square(alex, step)

w.mainloop()
