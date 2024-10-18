# Discussion Problem #1(c,e,g)
# (c)
# "p"
# (e)
# "ani"
# (g)
# "SPAM"

# Discussion Problem #2(a,d,e)
# (a)
# s1 = "spam"
# s2 = "ni!"
# print(s2[0:2].upper())
# (d)
# s1 = "spam"
# s2 = "ni!"
# print(s1)
# (e)
# s1 = "spam"
# s2 = "ni!"
# list = [s1[0:2], s1[3]]
# print(list)

# Discussion Problem #3(b,c,e)
# (b)
# Now
# is
# the
# winter
# of
# our
# discontent...
# (c)
# M ss ss pp
# (e)
# tfdsfu

# Write a program that uses five definite loops to produce the following single line of output
# Start the output with the variable name and opening quote
# print('grades = "', end='')
#
# for _ in range(60):
#     print('F', end='')
#
# for _ in range(10):
#     print('D', end='')
#
# for _ in range(10):
#     print('C', end='')
#
# for _ in range(10):
#     print('B', end='')
#
# for _ in range(10):
#     print('A', end='')
#
# print('"')

# Programming Exercise #3
# points = int(input("How many points? "))
# if 90 <= points <= 100:
#     grade = 'A'
# elif 80 <= points <= 89:
#     grade = 'B'
# elif 70 <= points <= 79:
#     grade = 'C'
# elif 60 <= points <= 69:
#     grade = 'D'
# else:
#     grade = 'F'
#
# print(f"The grade is: {grade}")

# Programming Exercise #4
sent = input("whats is the sentence? ").split()
for i in sent:
    print(i[0].upper(), end="")

# Programming Exercise #5
# name = input("Type in your name: ")
# total_number = 0
#
# for letter in name:
#     number = ord(letter.lower()) - ord('a') + 1
#     total_number+=number
#
# print(total_number)

