from turtle import *

a = Turtle()
b = Turtle()
screen = Screen()
screen.listen()
a.shapesize(3)


def move_forward():
    a.forward(10)


def move_backward():
    a.backward(10)


def move_left():
    new_heading = a.heading() + 10
    a.setheading(new_heading)


def move_right():
    new_heading = a.heading() - 10
    a.setheading(new_heading)


def clear_screen():
    a.clear()
    a.pu()
    a.goto(0, 0)
    # or a.home()
    a.pd()


screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.listen()
screen.exitonclick()