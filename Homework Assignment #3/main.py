from graphics import *

# 1)
# t = eval(input("How many numbers need to be summed "))
# n = 0
# for _ in range(t):
#     n += eval(input("Type a number "))
# print(f"The total sum is {n}")

# 2)
# t = eval(input("How many numbers need to be summed "))
# n = 0
# for _ in range(t):
#     n += eval(input("Type a number "))
# print(f"The average is {float(n/t)}")

# 3)
# Describe in your own words the object produced by each of the following
# operations from the graphics module. Be as precise as you can. Be sure to
# mention such things as the size, position, and appearance of the various
# objects. You may include a sketch if that helps.

# a)
# Point (130, 130)
# -------------------------------------------------------------------------------------------------
# point can represent a location. The first value is the x coordinate and the second one is y.
# It will produce a black dot/pixel on that specific coordinate

# b)
# c = Circle(Point(30,40) ,25)
# c.setFill("blue")
# c.setOutline("red")
# -------------------------------------------------------------------------------------------------
# This will draw out a circle at the coordinate x=30 and y=40 with a radius of 25 pixels stored in variable c
# It will fill the circle in with the color blue and outline it in the color red


# c)
# r = Rectangle(Point(20,20) , Point(40,40)) r.setFill(color_rgb(0,255, 150)) r.setWidth(3)
# -------------------------------------------------------------------------------------------------
# This will draw out a rectangle starting its upper left corner at x=20 and y=20 and finishing its lower right corner at x=40 and y=40 stored in the variable r
# The rectangle will be filled with a green color with a black border of 3 pixels width

# d)
# l = Line(Point(100, 100) , Point(100,200))
# l.setOutline("red4")
# l.setArrow('first')
# -------------------------------------------------------------------------------------------------
# This will start a line starting from x=100 and y=100 to x=100 and y=200 stored in the variable l.
# It'll will then be a red arrow that points north

# e)
# Oval(Point(50,50) , Point(60, 100))
# -------------------------------------------------------------------------------------------------
# This will create an oval shape that starts at coordinate x=50,y=50 ends x=60,y=100

# f)
# shape = Polygon(Point(5,5) , Point(10, 10) , Point(5,10) , Point(10,5))
# shape.setFill("orange")
# -------------------------------------------------------------------------------------------------
# This will create an hourglass shaped figure stored in a variable shape
# The way this works is that every point in the polygon function creates a new point where a position is assigned to
# it is filled with an orange color

# g)
# t = Text (Point (100, 100) , "Hello World! ")
# t.setFace("courier")
# t.setSize(16)
# t.setStyle('italic')
# -------------------------------------------------------------------------------------------------
# It creates a text at coordinate x=100,y=100 "Hello world". This is stored in a variable t
# The font is then courier with a size of 16px and the style of the text is set to Italic

# 4)
# First everything from the graphics library will be imported
# Then the program runs the main function which will do the following:
# It first stores the GraphWin function in a win variable.
# next it stores a created circle at x=50,y=50 with a radius of 20 in shape.
# This "shape" is outlined with red and filled with red and drawn in the GraphWin
# Then a for loop is created which runs the content code 10x
# p stores a function which waits untill the user clicks anywhere in the GUI
# c then gets the coordinate of the center of "shape"
# dx stores a value which subtracts the old x value (from c) from the new x value (from p)
# dy stores a value which subtracts the old y value (from c) from the new y value (from p)
# shape now moves dx pixels in the x and dy pixels in the y
# after done this ten times the GUI closes

# 5)
# win = GraphWin("Archery", 500, 500)
# colors = ["yellow", "red", "blue", "black", "white"]
# w = 25*6
# for color in reversed(colors):
#     w -= 25
#     c = Circle(Point(250,249) ,w)
#     c.setFill(color)
#     c.draw(win)
# win.getMouse()

# 6)
# win = GraphWin("Face", 500, 500)
# # face
# face = Oval(Point(125,50) , Point(375, 450))
# face.setFill("beige")
# face.draw(win)
# # mouth
# mouth = Polygon(Point(200,350) , Point(233,370) , Point(267,370) , Point(300,350), Point(267,330), Point(233,330))
# mouth.setFill("pink")
# mouth.draw(win)
# # eyes
# lx = 50
# rx = 150
# for _ in range(2):
#     lx += 100
#     rx += 100
#     eyes = Oval(Point(lx,150) , Point(rx, 200))
#     eyes.setFill("black")
#     eyes.draw(win)
# win.getMouse()

# 7)
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
# slope = dy/dx
# length = math.sqrt((dx**2)+(dy**2))
# print(f"The length is {length}.\nThe slope is {slope}")
# win.getMouse()
