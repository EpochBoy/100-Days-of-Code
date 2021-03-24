from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_move = 2
        self.y_move = 1.5

    def move_ball(self):
        new_x, new_y = self.xcor() + self.x_move, self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball(self):
        self.y_move *= -1

    def return_ball(self):
        self.x_move *= -1