import random
from turtle import Turtle

COLORS = ["red", "yellow", "blue", "green", "purple", "orange", "lime"]
INCREMENT_SPEED = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = 10
        self.cars = []
        self.create_cars()

    def create_cars(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=300, y=random.randint(-200, 200))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += INCREMENT_SPEED

