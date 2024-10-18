from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.pencolor("white")
        self.set_score()

    def set_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E   O V E R", align='center', font=('Arial', 18, 'normal'))
