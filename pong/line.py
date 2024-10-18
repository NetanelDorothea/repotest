from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,300)
        self.color("white")
        self.draw_line()

    def draw_line(self):
        self.setheading(270)
        for i in range(300):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
