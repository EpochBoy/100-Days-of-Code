# random walk challenge

from turtle import Turtle, Screen
from random import *

a = Turtle()
screen = Screen()
screen.colormode(1)
screen.colormode(255)
screen.screensize(800, 800)
a.speed(40)
a.pensize(6)

# walker logic aka. The AutisticPollock Turtle
for _ in range(1000):
    a.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    a.fillcolor(randint(1, 255), randint(1, 255), randint(1, 255))
    a.goto(randint(-800, 800), randint(-800, 800))


screen.exitonclick()