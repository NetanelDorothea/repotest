from turtle import Turtle
import random

START_AMOUNT = 10
LOOK_DIRECTION = 180
colors = [
    "#FF5733",  # Red-Orange
    "#33FF57",  # Green
    "#3357FF",  # Blue
    "#FF33A1",  # Pink
    "#FFD733",  # Yellow
    "#33FFF1",  # Cyan
    "#FF9A33",  # Orange
    "#B833FF",  # Purple
    "#33FF8A",  # Light Green
    "#FF3333",  # Red
    "#33A1FF",  # Light Blue
    "#C70039",  # Crimson
    "#900C3F",  # Dark Red
    "#FFC300",  # Bright Yellow
    "#DAF7A6",  # Light Lime
    "#581845",  # Dark Purple
    "#1F618D",  # Dark Blue
    "#17A589",  # Teal
    "#F5B041",  # Gold
    "#1ABC9C"  # Turquoise
]


class Cars():
    def __init__(self):
        super().__init__()
        self.difficulty = 1
        self.car_list = []
        self.create_cars()

    def create_cars(self):
        """creates the cars and put them on the starting position"""
        self.car_list = []
        for car in range(30):
            car = Turtle("square")
            car.color(random.choice(colors))
            car.setheading(180)
            car.shapesize(stretch_len=2)
            car.penup()
            car.goto(random.randrange(-300, 300), random.randrange(-240, 280, 25))
            self.car_list.append(car)

    def move_cars(self):
        """Makes the car move forward."""
        for car in self.car_list:
            car.showturtle()
            random_int = random.randint(1, self.difficulty)
            car.forward(random_int)
            if car.xcor() < -320:
                car.goto(280, random.randrange(-240, 280, 25))
