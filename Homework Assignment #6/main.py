# Chapter #7 - Discussion Problem #2
# It is similar because both are ways to prevent errors, the difference is that try/except checks for errors to handle
# on, while if statements handels condition and cannot used to detect datatypes

# Chapter  # 7 - Programming Exercise #3
# def grading(i):
#     if i >= 90:
#         return "A"
#     if i >= 80:
#         return "B"
#     if i >= 70:
#         return "C"
#     if i >= 60:
#         return "D"
#     else:
#         return "F"
#
# score = int(input("Whats the grade >> "))
# grade = grading(score)
# print(f"Grade is {grade}")

# Chapter #7 - Programming Exercise #7
# def convert_to_24hour(h, m, p):
#     """converts the time to 24 hour system and then to minutes. 'h' is hours, 'm' is minutes and 'p' is period"""
#     if p == "pm":
#         if h != 12:
#             h += 12
#
#     if p == "am":
#         if h == 12:
#             h = 0
#
#     # converting to military time format
#     mt = f"{h}:{m}"
#     return mt
#
#
# def calculate_lower_fee_time(mt):
#     """calculates the time in minutes in which the babysitter gets $1.75 an hour"""
#     mt = mt.split(':')
#
#     if int(mt[0]) >= 21:
#         mt[0] = int(mt[0]) - 21
#         reduced_fee_time = int(mt[0]) * 60 + int(mt[1])
#         return reduced_fee_time
#     else:
#         return 0
#
#
# def set_time(period):
#     """Manages time, for parameter 'period', choose 'starting' or 'ending'"""
#     time_check = True
#     while time_check:
#         # input in hours
#         time_h = int(input(f"{period.title()} time hour >> "))
#
#         if 0 < time_h <= 12:
#             break
#         else:
#             print("Something went wrong. Try again")
#
#     while time_check:
#         # input in minutes
#         time_m = int(input(f"{period.title()} time minute >> "))
#
#         if 0 <= time_m <= 59:
#             if time_m < 10:
#                 time_m = f"0{time_m}"
#             break
#         else:
#             print("Something went wrong. Try again")
#
#     while time_check:
#         # "nd" for night/day
#         nd = input("AM or PM >> ").lower()
#         if nd == "am" or nd == "pm":
#             break
#         else:
#             print("Something went wrong. Try again")
#
#     # print(f"\n{period.title()} time was {time_h}:{time_m}{nd}")
#
#     # converts to military time for calculation convience
#     time_military = convert_to_24hour(time_h, time_m, nd)
#     # print(f"Military time is {time_military}\n")
#
#     # returns Lower Paid time in minutes
#     lp_time = calculate_lower_fee_time(time_military)
#
#     return time_military, lp_time
#     # return convert_time_minute(time_h, int(time_m), nd)
#
#
# def calculate_bill(s_time, e_time):
#     # low fee time in minutes
#     start_low_fee_m = s_time[1]
#     end_low_fee_m = e_time[1]
#
#     # hour in minutes
#     start_time = s_time[0].split(':')
#     start_mins = int(start_time[0]) * 60 + int(start_time[1])
#     end_time = e_time[0].split(':')
#     end_mins = int(end_time[0]) * 60 + int(end_time[1])
#
#     # CALCULATIONS |
#     # total worked hours in minutes and hours
#     total_time_m = end_mins - start_mins
#     total_time_h = total_time_m / 60
#     # total time worked with reduced fee
#     total_time_rf = end_low_fee_m - start_low_fee_m
#     total_time_rf /= 60
#     # total amount $
#     total_bill = total_time_h * 2.50
#     reduced_bill = total_time_rf * 0.75
#     total_bill -= reduced_bill
#
#     return "{:.2f}".format(total_bill)
#
#
# starting_time = set_time("starting")
# ending_time = set_time("ending")
# total_bill = calculate_bill(starting_time, ending_time)
#
# print(f"Total bill is ${total_bill}")

# Chapter #7 - Programming Exercise #8
# age = int(input("What is your age? >> "))
# if age >= 27:
#     years = int(input("How many years have you been a citizen? >> "))
#     if years >= 7:
#         print("You are eligible to be a US representative")
#         if years >= 9 and age >= 30:
#             print("You are also eligible to be a US senator")
#     else:
#         print("Sorry, you need more years of citizenship to be eligible for the Senate and the House")
# else:
#     print("Sorry, you are too young to be eligible for the Senate and the House")


# Modify a program from a previous homework assignment so that it utilizes exception handling to prevent at least two
# conceivable run-time errors. Explain what these errors are and how the program will respond.
# Programming Exercise #14 from Chapter #3
# try:
#     times = int(input("How many numbers? "))
#
# except ValueError:
#     print('No number was given')
#     times = 0
# """
# So valueError means that the wrong datatype is given. It wants the input to be an integer as seen by the int() function
# and that is why this message is poppin up:
# Traceback (most recent call last):
#   File "..\main.py", line 144, in <module>
#     times = int(input("How many numbers? "))
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'p'
# """

# sum_numbers = 0
#
# def avg_number(sum_numbers, divide):
#     try:
#         avg_number = sum_numbers / divide
#     except ZeroDivisionError:
#         avg_number = 0
#     """
#     ZeroDivisionError means that the program is trying to divide a number by 0. This is of course not possible and
#     therefore it gives the error message:
#     Traceback (most recent call last):
#       File "..\main.py", line 171, in <module>
#         avg = avg_number(sum_numbers, times)
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#       File "..\main.py", line 159, in avg_number
#         avg_number = sum_numbers / divide
#                      ~~~~~~~~~~~~^~~~~~~~
#     ZeroDivisionError: division by zero
#     """
#     return float(avg_number)
#
#
# for i in range(times):
#     number = eval(input(f"#{i + 1} choose a number "))
#     sum_numbers += number
# avg = avg_number(sum_numbers, times)
# print(f"the average is {avg}.")
