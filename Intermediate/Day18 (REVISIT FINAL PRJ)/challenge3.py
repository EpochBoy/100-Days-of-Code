from turtle import Turtle, Screen
import random

a = Turtle()
dist = 100

# # Drawing shapes
# # Draw a triangle
# sides = 3
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)
# # Draw a square
# sides = 4
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)
# # Draw a pentagon
# sides = 5
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)

# # Draw a hexagon
# sides = 6
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)
# # Draw a heptagon
# sides = 7
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)
# # Draw an octagon
# sides = 8
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)
# # Draw a nonagon
# sides = 9
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)
# # Draw a decagon
# sides = 10
# angle = 360 / sides
# for _ in range(sides):
#     a.forward(dist)
#     a.right(angle)

# Let's make the above a loop instead & add custom colors
screen = Screen()
screen.colormode(1)
screen.colormode(255)

for i in range(3, 11):
    sides = i
    angle = 360 / sides
    a.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    a.pensize(2)
    for j in range(i):
        a.forward(dist)
        a.right(angle)

screen.exitonclick()