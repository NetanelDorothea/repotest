from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.start_pos = 0
        self.dir = 0
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]

    def add_segment(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_segment.append(snake)

    def create_snake(self):
        """Creates the starting segments in the snake"""
        for _ in range(3):
            self.add_segment((self.start_pos, 0))
            self.start_pos += -MOVE_DISTANCE

    def extend(self):
        self.add_segment(self.snake_segment[-1].pos())

    def move(self):
        """Lets the snake move forward"""
        for index in range(len(self.snake_segment) - 1, 0, -1):
            next_pos = self.snake_segment[index - 1].pos()
            self.snake_segment[index].goto(next_pos)
        self.head.forward(MOVE_DISTANCE)
        # print(self.head.tilt)

    def eat(self, snake_color):
        self.extend()
        for seg in self.snake_segment:
            seg.color(snake_color)

    def up(self):
        if not self.dir == 270:
            self.dir = 90
            self.head.setheading(self.dir)

    def down(self):
        if not self.dir == 90:
            self.dir = 270
            self.head.setheading(self.dir)

    def left(self):
        if not self.dir == 0:
            self.dir = 180
            self.head.setheading(self.dir)

    def right(self):
        if not self.dir == 180:
            self.dir = 0
            self.head.setheading(self.dir)
