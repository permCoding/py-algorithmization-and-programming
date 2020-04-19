names = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
pos_name = 4
bgcolor = 'lightgreen'
fgcolor = '#4400AA'
speed = 1
pensize = 3


def square(t, step):
    t.pendown()
    for _ in range(4):
        t.forward(step)
        t.right(90)
    t.penup()


def change_pos(t, x, y):
    t.speed(0)
    t.penup()
    # t.setpos(-199, +199)
    # t.setpos(-width//2+10, +height//2-10)
    t.goto(x, y)
    # t.setx(-200)
    t.speed(speed)
