from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(x_pos, y_pos)

    def move_up(self):
        new_y_pos = self.ycor() + 20
        self.goto(self.xcor(), new_y_pos)

    def move_down(self):
        new_y_pos = self.ycor() - 20
        self.goto(self.xcor(), new_y_pos)
