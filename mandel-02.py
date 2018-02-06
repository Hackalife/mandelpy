import turtle
i = 0
position = 0

for i in range(0, 1000):

    turtle.forward(i*4)
    turtle.right(15)
    position = turtle.pos()
    turtle.goto(0,0)
    turtle.goto(position)
    turtle.right(90)
    turtle.forward(i)
    turtle.speed(50)
pass
