import random
import turtle

# import colorgram
#
# colors = colorgram.extract('hirst-paint.jpg', 40)
#
# i = 0
# color_list = []
#
# for _ in colors:
#     color_combo = colors[i]
#     rgb = color_combo.rgb
#     rgb_tuple = (rgb.r, rgb.g, rgb.b)
#     color_list.append(rgb_tuple)
#     i += 1

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154),
              (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8),
              (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
              (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42),
              (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14),
              (38, 43, 221)]

x_pos = -250
y_pos = -250
t = turtle.Turtle()
screen = turtle.Screen()
t.pensize(20)
turtle.colormode(255)
t.shape("turtle")
t.speed("fastest")


def random_color():
    i = random.choice(color_list)
    # t.pencolor(i)
    return i


def draw():
    for _ in range(10):
        t.dot(20, random_color())
        t.forward(50)


def start_turtle():
    t.penup()
    global y_pos
    for _ in range(10):
        t.goto(x_pos, y_pos)
        draw()
        y_pos += 50
    t.hideturtle()

start_turtle()
screen.exitonclick()
