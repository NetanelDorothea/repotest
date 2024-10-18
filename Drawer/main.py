import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
color_list = ["red", "blue", "green", "purple", "black", "gold"]

player_red = Turtle()
player_blue = Turtle()
player_green = Turtle()
player_purple = Turtle()
player_black = Turtle()
player_gold = Turtle()

player_list = [player_red, player_blue, player_green, player_purple, player_black, player_gold]

play = True


def turtle_run(player):
    global play
    steps = random.randint(0, 10)
    player.forward(steps)
    if player.xcor() > 229:
        play = False
        return print(f"{player.pencolor()} won!")


def initial_settings():
    turtle.hideturtle()
    y_pos = 360 / 6
    screen.setup(width=500, height=400)
    i = 0
    for player in player_list:
        player.speed(9)
        player.penup()
        player.color(color_list[i])
        player.shape("turtle")
        player.goto(x=-230, y=y_pos * i - 180 + 30)
        i += 1
        player.speed("normal")


def play_game():
    global play
    initial_settings()
    input = screen.textinput("Guess the winner!", "Which turtle do you think will win?")
    print(f"Your guess was {input}...")
    play = True
    while play:
        for player in player_list:
            turtle_run(player)
    screen.onkey(fun=play_game, key="space")
    screen.listen()
    screen.exitonclick()


play_game()
