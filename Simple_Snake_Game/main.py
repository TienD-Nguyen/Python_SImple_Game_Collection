import time
from turtle import Screen
from snake import Snake
from food import Food
from board import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_left, "Left")

screen.update()

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.09)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_board()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[2:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_board()
            snake.reset()


screen.exitonclick()
