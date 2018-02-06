import turtle
i = 0
position = 0

for i in range(0, 1000):

    def returnHome():

        position = turtle.pos()
        turtle.goto(0,0)
        turtle.goto(position)
    pass

    def tf(dist):
        turtle.forward(dist)
    pass

    tf(i)
    turtle.right(45)
    tf(i*5)
    returnHome()
    turtle.goto(i*4,0)


pass
