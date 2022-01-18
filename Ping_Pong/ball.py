from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.y_move = MOVE_DISTANCE
        self.x_move = MOVE_DISTANCE
        self.penup()

    def move(self):
        self.goto(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.bounce_x()

