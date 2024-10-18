from turtle import Screen
from players import Players
from ball import Ball
from score import Score
from line import Line
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

player1 = Players((350, 0))
player2 = Players((-350, 0))
ball = Ball()
score = Score()
line = Line()

screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game_is_running = True
while game_is_running:
    screen.update()
    if ball.move():
        if ball.distance(player1) < 60:
            print("received")
        elif ball.distance(player2) < 60:
            print("received")
        else:
            if ball.xcor() > 350:
                score.change_score(0,1)
            elif ball.xcor() < -350:
                score.change_score(1,0)
            ball.reset()

    time.sleep(0.1)

screen.exitonclick()
