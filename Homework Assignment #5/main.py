# Chapter #6 - Programming Exercise #1
# animal_list = {
#     "cow": "moo, moo",
#     "cat": "miauw, miauw",
#     "dog": "bark, bark",
#     "bird": "chirp, chirp",
#     "pig": "knorr, knorr"
# }
#
#
# def refrein():
#     print("Old Macdonald had a farm, Ee-igh, Ee-igh, Oh!")
#
#
# def lyrics(animal):
#     refrein()
#     print(f"And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh! ")
#     print(f"With a {animal_list[animal]} here and a {animal_list[animal]} there.")
#     print(
#         f"Here a {animal_list[animal].split(' ')[0]} there a {animal_list[animal].split(' ')[0]} everywhere a {animal_list[animal]}.")
#     refrein()
#
#
# def sing():
#     for animal in animal_list:
#         print("\n")
#         lyrics(animal)
#
#
# sing()

# Programming Exercise #14 from Chapter #3
# times = int(input("How many numbers? "))
# sum_numbers = 0
#
#
# def avg_number(sum_numbers, divide):
#     avg_number = sum_numbers / divide
#     return float(avg_number)
#
#
# for i in range(times):
#     number = eval(input(f"#{i + 1} choose a number "))
#     sum_numbers += number
# avg = avg_number(sum_numbers, times)
# print(f"the average is {avg}.")

# Programming Exercise #8 from Chapter #4
# from graphics import *
# import math
# win = GraphWin()
# point1 = win.getMouse()
# x1 = point1.getX()
# y1 = point1.getY()
# point2 = win.getMouse()
# x2 = point2.getX()
# y2 = point2.getY()
# l = Line(Point(x1, y1), Point(x2,y2))
# l.draw(win)
# l_cor = l.getCenter()
# l_cor = Point(l_cor.getX(), l_cor.getY()).draw(win)
# l_cor.setFill("cyan")
# dx = x2 - x1
# dy = y2 - y1
#
# def calc_slope(dy, dx):
#     slope = dy/dx
#     return slope
#
# def calc_distance(dy, dx):
#     length = math.sqrt((dx**2)+(dy**2))
#     return length
#
# slope = calc_slope(dy, dx)
# distance = calc_distance(dy, dx)
# print(f"The distance is {distance}.\nThe slope is {slope}")
# win.getMouse()

# Chapter  # 6 - Programming Exercise #12
# nums = [1,2,3,4,5,]
#
# def sumlist(nums):
#     sum_value = 0
#     for i in nums:
#         sum_value += i
#     return sum_value
#
# print(sumlist(nums))

# (5)
# string_amount = int(input("How many strings? "))
# s_list = []
#
# def get_some_strings(x):
#     for i in range(x):
#         s = input(f"What is sentence #{i+1}? ")
#         s_list.append(s)
#     return s_list
#
# print(get_some_strings(string_amount))