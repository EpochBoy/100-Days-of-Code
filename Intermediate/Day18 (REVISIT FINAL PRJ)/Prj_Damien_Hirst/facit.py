import colorgram

colors = colorgram.extract("hirstpainting.jpg", 30)
converted_color = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    temp = (r, g, b)
    converted_color.append(temp)

import turtle as turtle_module
import random

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

tim = turtle_module.Turtle()
turtle_module.colormode(255)
screen = turtle_module.Screen()
# screen.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed(20)
tim.hideturtle()

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(30, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()