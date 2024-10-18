import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

direction = [0, 90, 180, 270]
t.pensize(3)
turtle.colormode(255)

t.shape("turtle")
t.speed("fastest")


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def circle():
    for _ in range(72):
        # t.setheading(random.choice(direction))
        t.right(5)
        t.forward(10)


for _ in range(36):
    t.color(randomcolor())
    t.right(32)
    circle()
screen.exitonclick()
