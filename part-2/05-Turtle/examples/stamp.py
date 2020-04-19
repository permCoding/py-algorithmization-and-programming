import turtle

w = turtle.Screen()
w.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("#4400AA")
alex.speed(3)
alex.penup()

step = 15 # длина шага
count = 35 # кол-во шагов
for i in range(count):
    alex.stamp() # оставить отпечаток
    step += 4 # увеличить шаг
    alex.forward(step) # вперёд
    alex.right(33) # повернуть

w.mainloop()