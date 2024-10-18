import time
from turtle import Screen
from player import Player
from car_manager import Cars
from score import Score

screen = Screen()
screen.title("Crossy Road")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car = Cars()
score = Score()

screen.onkey(player.go_forward, "space")
screen.onkey(player.go_forward, "Up")

game_is_running = True
while game_is_running:
    if player.ycor() > 300:
        car.difficulty *= 2
        print(car.difficulty)
        player.turtle_reset()
        score.level += 1
        score.set_score()
    car.move_cars()
    screen.update()

    for i in car.car_list:
        if player.distance(i) < 21:
            score.game_over()
            game_is_running = False


    time.sleep(0.05)

screen.exitonclick()
