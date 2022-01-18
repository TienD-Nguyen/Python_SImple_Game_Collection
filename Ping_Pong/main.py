from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_STARTING_POSITION = [(-420, 0), (420, 0)]

screen = Screen()
screen.bgcolor("black")
screen.title("My Ping Pong Game")
screen.setup(width=900, height=600)
screen.tracer(0)

l_paddle = Paddle(PADDLE_STARTING_POSITION[0])
r_paddle = Paddle(PADDLE_STARTING_POSITION[1])
ball = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_over = True
while game_is_over:
    screen.update()
    time.sleep(0.04)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.ycor() < -380 or ball.distance(r_paddle) < 50 and ball.xcor() > 380:
        ball.bounce_x()

    if ball.xcor() > 450:
        ball.reset_position()
        score_board.r_score_up()

    if ball.xcor() < -450:
        ball.reset_position()
        score_board.l_score_up()

screen.exitonclick()