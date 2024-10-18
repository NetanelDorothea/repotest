# (10pts) Discussion Question 1 (pg. 278)
# Compare and contrast the following pairs of terms:
# a)
# definite loop vs. indefinite loop:
# the number of iterations is determined when the loop starts in a definite loop
# An indefinite loop keeps iterating until certain conditions are met. There is no guarantee ahead of time regarding
# how many times the loop will go around.
# b)
# for loop vs. while loop
# for loop is an definite loop while a while loop is indefinite. You can give a value for a for loop on how many times
# you want it to loop. The while loop loops until certain conditions are met
# c)
# interactive loop vs. sentinel loop
# an interactive loop is that it allows the user to repeat certain portions of a loop Structures and Booleans program on
# demand.
# A sentinel loop continues to process data until reaching a special value that signals the end. the sentinel should be
# distinguishable from actual data values
# d)
# sentinel loop vs. end -of-file loop
# A sentinel loop continues to process data until reaching a special value that signals the end.
# -of-file loop ends until the end of a file is reached
# It could be so that the end of the file could be a value for the sentinel

# (10pts) Discussion Question 2 (all sub-problems) (pg. 278/279)
# a)
# 1 p = F  q = F result = False
# 2 p = F  q = T  result = True
# 3 p = T  q = F  result = True
# 4 p = T  q = T  result = False
# b)
# 1 p = F  q = F result = False
# 2 p = F  q = T  result = True
# 3 p = T  q = F  result = False
# 4 p = T  q = T  result = False
# c)
# 1 p = F  q = F result = True
# 2 p = F  q = T  result = True
# 3 p = T  q = F  result = True
# 4 p = T  q = T  result = False
# d)
# 1 p = F  q = F  r = F result = False
# 2 p = F  q = T  r = T  result = True
# 3 p = T  q = F  r = T  result = True
# 4 p = T  q = T  r = F result = True
# 5 p = T  q = F  r = F  result = False
# 6 p = F  q = T  r = F  result = False
# 7 p = F  q = F  r = T  result = true
# 8 p = T  q = T  r = T  result = True
# e)
# 1 p = F  q = F  r = F result = False
# 2 p = F  q = T  r = T  result = True
# 3 p = T  q = F  r = T  result = True
# 4 p = T  q = T  r = F result = True
# 5 p = T  q = F  r = F  result = False
# 6 p = F  q = T  r = F  result = False
# 7 p = F  q = F  r = T  result = True
# 8 p = T  q = T  r = T  result = True

# (10pts) Discussion Question 3 (a,c) (pg. 279)
# a)
# n = int(input("Type number >> "))
# total = 0
# for i in range(n):
#     total += i+1
#
# c)
# total = 0
# while True:
#     n = int(input("Type number >> "))
#     if n == 999:
#         break
#     total += n
# print(total)


# (10pts) Programming Exercise 1 (pg. 279)
# n = -1
#
# while not n >= 0:
#     try:
#         n = int(input("number >> "))
#     except ValueError:
#         n = -1
#
# n1 = 0
# n2 = 1
#
# n_phrase = ""
# for _ in range(n):
#     n_phrase += f"{n2}, "
#     n3 = n2
#     n2 += n1
#     n1 = n3
#
# print(f"{n_phrase}...")


# (10pts) Programming Exercise 4 (pg. 280)
def syr(x):
    seq = f"{x}"
    while not x < 2:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
        seq += f", {int(x)}"
    return seq


x = -1
while not x >= 0:
    try:
        x = int(input("number >> "))
    except ValueError:
        n = -1
print(syr(x))
