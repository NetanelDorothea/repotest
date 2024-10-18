from turtle import Turtle

FORWARD_STEPS = 25
STARTING_POS = (0, -269)
LOOK_DIRECTION = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.8)
        self.penup()
        self.color("green")
        self.setheading(LOOK_DIRECTION)
        self.turtle_reset()

    def go_forward(self):
        self.forward(FORWARD_STEPS)

    def turtle_reset(self):
        self.goto(STARTING_POS)
