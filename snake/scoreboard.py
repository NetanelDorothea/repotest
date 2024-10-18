from turtle import Turtle

ALIGNMENT = "center"
FONT = ('robot', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.points = 0
        self.goto(0, 260)
        self.change_score(self.points)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def change_score(self, add):
        self.clear()
        self.points += add
        self.write(f"Score = {self.points}", align=ALIGNMENT, font=FONT)
