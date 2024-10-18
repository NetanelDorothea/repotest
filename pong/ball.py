from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed = 10
        self.penup()
        self.yspeed = random.randint(-20, 20)
        self.xspeed = 10
        self.vert_steps = 0
        self.hor_steps = 0

    def move(self):
        total_speed = abs(self.xspeed) + abs(self.yspeed)
        self.vert_steps = self.yspeed / total_speed
        self.hor_steps = self.xspeed / total_speed
        for step in range(1, int(total_speed + 1)):
            self.goto(self.xcor() + self.hor_steps, self.ycor() + self.vert_steps)
            if self.touching_edge():
                return True

    def touching_edge(self):
        """rules for when edge is touched"""
        if self.ycor() > 280 or self.ycor() < -280:
            self.yspeed += (self.yspeed / abs(self.yspeed))
            self.yspeed *= -1
            self.vert_steps *= -1

        if self.xcor() > 350 or self.xcor() < -350:
            self.xspeed += (self.xspeed / abs(self.xspeed))
            self.xspeed *= -1
            self.hor_steps *= -1
            print(f"speed = {self.xspeed}")
            return True

    def reset(self):
        self.goto(0,0)
        self.yspeed = random.randint(-20, 20)
        self.xspeed = 10

