import turtle

def goU():
    turtle.setheading(90)
    turtle.forward(step)
def goR():
    turtle.setheading(0)
    turtle.forward(step)
def goD():
    turtle.setheading(270)
    turtle.forward(step)
def goL():
    turtle.setheading(180)
    turtle.forward(step)


turtle.reset()
turtle.shape('turtle')
turtle.bgcolor('#009944')
turtle.turtlesize(2)
turtle.pencolor('yellow')

sp = int(turtle.numinput('Вопрос', 'Введите скорость: ', default=2))
step = 50
turtle.speed(sp)
turtle.pendown() # Опускаем перо перо (начало рисования)
turtle.onkey(goU,"Up")
turtle.onkey(goR,"Right")
turtle.onkey(goD,"Down")
turtle.onkey(goL,"Left")
turtle.listen() # Включить прослушивание событий
turtle.penup() # Поднять перо (закончить рисовать)

turtle.mainloop() # Задержать окно на экране