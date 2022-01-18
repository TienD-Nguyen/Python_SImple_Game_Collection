from turtle import Turtle

MOVE_DISTANCE = 10


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(starting_position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)