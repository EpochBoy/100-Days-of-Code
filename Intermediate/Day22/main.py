#  Score side-by-side
# Player/paddle class
# Map class
# Ball

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)
ball = Ball(0, 0)

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.pu()
# paddle.goto(350, 0)


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)


# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "w")
screen.onkey(right_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    ball.move_ball()
    screen.update()

    # ball collision detection
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce_ball()
    if ball.xcor() > 305:
        if ball.ycor() > right_paddle.ycor():
            ball.return_ball()
    if ball.xcor() < -305:
        if ball.ycor() > left_paddle.ycor():
            ball.return_ball()


# screen.exitonclick()