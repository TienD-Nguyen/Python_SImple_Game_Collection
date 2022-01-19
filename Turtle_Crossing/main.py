import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.04)

    car_manager.create_cars()
    car_manager.move()

    if player.is_at_finish():
        player.refresh()
        car_manager.increase_speed()
        scoreboard.level_up()

    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()