from turtle import Turtle


class Players(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.movement_speed = 20
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(start_pos)

    def go_up(self):
        self.sety(self.ycor() + self.movement_speed)

    def go_down(self):
        self.sety(self.ycor() - self.movement_speed)
