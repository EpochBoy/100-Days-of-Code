from turtle import Turtle, Screen
from random import *


a = Turtle()
screen = Screen()
a.speed("fastest")
a.pensize(2)
screen.colormode(1)
screen.colormode(255)

size = 5
for i in range(1, int(360 / size)):
    a.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    a.fillcolor(randint(1, 255), randint(1, 255), randint(1, 255))
    a.circle(100)
    a.setheading(a.heading() + size)


screen.exitonclick()