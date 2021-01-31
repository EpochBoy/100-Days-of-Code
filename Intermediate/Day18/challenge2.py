# from turtle import Turtle, Screen

# # accessed this way
# turtle = Turtle()

# # or
# from turtle import *

# # accessed this way
# Turtle()

# # or
# import turtle

# # accessed this way
# tim = turtle.Turtle()

# # or
# import turtle as tur

# # accessed this way
# tim = tur.Turtle()


# turtle.shape("turtle")
# turtle.color("red")

# Draw turtle square with turtle
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

# Same using turtle loop
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)


# Modules that aren't packaged with python standard library
# use pip (python packages) See: https://pypi.org
# terminal: 'pip install heroes'

# import heroes

# print(heroes.gen())

# Assignment "Draw a dashed line for 50 paces"
from turtle import Turtle, Screen

a = Turtle()

# for i in range(25):
#     a.pd()
#     a.pensize(2)
#     a.forward(5)
#     for j in range(25):
#         a.pu()
#         a.forward(0.5)

# or
for _ in range(15):
    a.pd()
    a.pensize(1)
    a.forward(5)
    a.pu()
    a.forward(5)

screen = Screen()
screen.exitonclick()
