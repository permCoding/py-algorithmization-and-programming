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


def t_move_left(x,y):
    goL()
def t_move_right(x,y):
    goR()
def t_move_up(x, y):
    goU()
def t_move_down(x, y):
    goD()

turtle.reset()
turtle.shape('turtle')
turtle.bgcolor('#009944')
turtle.turtlesize(2)
turtle.pencolor('yellow')

sp = int(turtle.numinput('Вопрос', 'Введите скорость: ', default=2))
step = 50
turtle.speed(sp)
turtle.pendown()  # Опускаем перо перо (начало рисования)

turtle.onkey(goU, "Up")
turtle.onkey(goR, "Right")
turtle.onkey(goD, "Down")
turtle.onkey(goL, "Left")

turtle.onclick(t_move_left, 1)
turtle.onclick(t_move_right, 3)

turtle.onscreenclick(t_move_up, 1)
turtle.onscreenclick(t_move_down, 3)

turtle.listen() # Включить прослушивание событий
turtle.penup() # Поднять перо (закончить рисовать)

turtle.mainloop() # Задержать окно на экране
