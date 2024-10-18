# 1) downloaded python

# 2a)
# Everything is within a string including the comma
print("Hello, world! ")
# Two string types are being separate by the comma
print("Hello", "world!")
# 2b)
# Is an integer '3'
print(3)
# Is a float-point number '3.0'
print(3.0)
# 2c)
# Two integers getting summed creating the integer '5'
print(2 + 3)
# Two float-point numbers getting summed creating the float '5.0'
print(2.0 + 3.0)
# Two strings getting added to each other creating the string '23'
print("2" + "3")
# 2d)
# basic multiplication creating the intnumber '6'
print(2 * 3)
# same as 2 to the power of 3 resulting in 8
print(2 ** 3)
# 2e)
# division resulting in float number 2.333...
print(7 / 3)
# '//' is floor division. In this case resulting in 0 since 2/3 is 0.6 and the floor of 0.6 is 0
print(2 // 3)

# 3)
x = eval(input("Enter a number between 0 and 1: "))
n = eval(input("How many numbers should I print? "))
for _ in range(n):
    x = 3.9 * x * (1 - x)
    print(x)

# 4)
kilometer = eval(input('How many kilometers? '))
print(f'{kilometer}km is {kilometer * 0.62} miles')

# 5)
p = 10000
r = 0.08
n = 12
t = eval(input("How many years: "))
a = p * (1 + (r / n)) ** (n * t)
print(a)
