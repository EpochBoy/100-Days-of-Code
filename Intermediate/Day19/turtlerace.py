from turtle import *
import random

colors = ["red", "blue", "green", "yellow", "orange", "black"]
screen = Screen()
screen.listen()
screen.setup(1000, 1000)
user_bet = screen.textinput(
    title="What is your bet?", prompt="Which turtle will win the race? Enter a color: "
)

x = -450
y = -200
is_race_on = False

race_team = []
for i in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(i)
    turtle.pu()
    turtle.goto(x, y)
    y += 100
    race_team.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in race_team:
        distance = random.randint(0, 40)
        if i.xcor() > 450:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won. {winning_color} came first!")
            else:
                print(f"You've lost. {winning_color} came first!")
        i.forward(distance)


screen.listen()
screen.exitonclick()