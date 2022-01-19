from turtle import Turtle

START_POSITION = (0, -280)
MOVING_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(self.heading() + 90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVING_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVING_DISTANCE)

    def refresh(self):
        self.goto(START_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False