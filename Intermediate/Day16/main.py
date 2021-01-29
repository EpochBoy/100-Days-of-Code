# OOP

# Importing turtle library
import turtle
from turtle import Turtle

# Creating new objects from Class Turtle
timmy = turtle.Turtle()
tommy = Turtle()

# modifying instance of turtle
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.turtlesize(2)

# Printing objects
print(timmy)
print(tommy)

my_screen = turtle.Screen()

# Printing properties of Screen()'s canvas
print(my_screen.canvheight)
print(my_screen.canvwidth)

my_screen.exitonclick()
