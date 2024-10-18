from turtle import Screen
import time
import snake
from scoreboard import Scoreboard
from food import Food

snake = snake.Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

game_is_running = True

while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.change_score(1)
        color = food.refresh()
        snake.eat(color)

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_running = False
        score.game_over()

    for seg in snake.snake_segment[1:len(snake.snake_segment)]:
        if snake.head.distance(seg) < 15:
            game_is_running = False
            score.game_over()
screen.exitonclick()
