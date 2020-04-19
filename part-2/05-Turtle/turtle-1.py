import turtle

names = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

w = turtle.Screen()
w.bgcolor("lightgreen")

alex = turtle.Turtle()
pos_name = 4
alex.shape(names[pos_name])

alex.color("#4400AA")
alex.speed(1)
alex.pensize(3)

step = 100

alex.pendown()
alex.forward(step)
alex.right(90)
alex.forward(step)
alex.right(90)
alex.penup()
alex.forward(step)
alex.right(90)
alex.pendown()
alex.forward(step)

w.mainloop()
