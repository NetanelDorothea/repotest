# 1a =
# 0
# 1
# 4
# 9
# 16

# 1b = 3 1 4 1 5

# 1c =
# Hello
# Hello
# Hello
# Hello

# 1d =
# 0 1
# 1 2
# 2 4
# 3 8
# 4 16

# 2a =
# 7.4

# 2c =
# 8

# 2e =
# 11

# 3b =
# (n* (n-1)) / 2

# 3c =
# 4*math.pi*r**2

# 4b =
# 1 : 1
# 3 : 27
# 5 : 125
# 7 : 343
# 9 : 729
# 9

# 4c =
# 012
# 212
# 412
# 612
# 812
# done

# 5 =
x1 = eval(input("What's the first x coordinate "))
y1 = eval(input("What's the first y coordinate "))
x2 = eval(input("What's the second x coordinate "))
y2 = eval(input("What's the second y coordinate "))
if not x1 == x2:
    slope = (y2 - y1) / (x2 - x1)
    print(slope)

#6 =
import math
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist)