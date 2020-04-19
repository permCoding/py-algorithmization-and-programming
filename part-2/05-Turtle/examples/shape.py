from turtle import *

speed(8)
color('red', 'yellow')
begin_fill()
while True:
    forward(250)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()