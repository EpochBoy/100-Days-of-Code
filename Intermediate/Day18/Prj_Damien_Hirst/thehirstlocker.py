# install colorgram using pip

import colorgram

colors = colorgram.extract("hirstpainting.jpg", 30)
converted_color = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    temp = (r, g, b)
    converted_color.append(temp)
# Chosen colors
color_list = [
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (198, 91, 71),
    (46, 122, 86),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (183, 205, 171),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (174, 94, 97),
]

from turtle import *
from random import *

hirst = Turtle(visible=False)
screen = Screen()
screen.colormode(1)
screen.colormode(255)
screen.screensize(400, 400)
hirst.speed(40)
hirst.pensize(6)


def circle_maker():
    color = color_list[randint(0, len(color_list) - 1)]
    hirst.pu()
    hirst.dot(50, color)
    # hirst.fd(50)


def start():
    x = -750
    y = -450
    for i in range(20):
        hirst.pu()
        hirst.goto(x, y)
        x += 75
        circle_maker()
    for i in range(12):
        hirst.pu()
        hirst.goto(x, y)
        circle_maker()
        y += 75
        x = -750
        for j in range(20):
            hirst.pu()
            hirst.goto(x, y)
            x += 75
            circle_maker()
    hirst.pu()
    hirst.goto(x, y)
    x += 75
    circle_maker()


start()

screen.exitonclick()