from turtle import Turtle
import random

random_clist = ["red", "green", "blue", "cyan", "green", "magenta", "white", "yellow"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("white")
        self.refresh()

    def refresh(self):
        old_color = self.pencolor()
        random_color = random.choice(random_clist)
        self.color(random_color)
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)
        return old_color
