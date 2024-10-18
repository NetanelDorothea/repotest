# from turtle import Turtle, Screen
#
# jimmy = Turtle()
# jimmy.shape("turtle")
# jimmy.color("red")
#
# for i in range(10):
#     jimmy.forward(10)
#
# my_screen = Screen()
# my_screen.exitonclick()

pokemon = {
    'pikachu': 'electric',
    'Squirtel': 'Water',
    'Charmanader': 'Fire'
}

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemome Name", ['pikachu', 'Squirtel', 'Charmanader'])
table.add_column("Type", ['electric', 'Water', 'Fire'])

table.align = "l"
print(table)
