from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_list = []
        self.create_scores()
        self.player1_score = 0
        self.player2_score = 0
        self.change_score(points1=self.player1_score, points2=self.player2_score)

    def create_scores(self):
        for i in range(2):
            score = Turtle()
            score.hideturtle()
            score.penup()
            score.color("white")
            self.score_list.append(score)
        self.positioning()

    def positioning(self):
        self.score_list[0].goto(80, 150)
        self.score_list[1].goto(-80, 150)

    def change_score(self, points1, points2):
        self.positioning()
        self.player1_score += points1
        self.player2_score += points2
        self.score_list[0].clear()
        self.score_list[0].write(f"{self.player1_score}", True, align="center", font=('Arial', 100, 'normal'))
        self.score_list[1].clear()
        self.score_list[1].write(f"{self.player2_score}", True, align="center", font=('Arial', 100, 'normal'))
