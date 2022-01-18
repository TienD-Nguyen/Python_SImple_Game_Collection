from turtle import Turtle

FONT = ("Courier", 52 , "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(75, 240)
        self.write(f"{self.r_point}", align="center", font=FONT)
        self.goto(-75, 240)
        self.write(f"{self.l_point}", align="center", font=FONT)

    def l_score_up(self):
        self.l_point += 1
        self.update_scoreboard()

    def r_score_up(self):
        self.r_point += 1
        self.update_scoreboard()