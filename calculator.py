"""
calculator.py

Using our arithmetic.py file from Euser_entryercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
math_functions = ['+', '-', '*', '/', '%', '**2', "**3", "**" ]
user_entry = raw_input("Please type an arithmetic function followed by 2 numbers. ")
# Your code goes here
while True:

    user_entry.split(" ")
    # user_entry[1] = (user_entry[1])
    # user_entry[2] = (user_entry[2])
    if user_entry[0] == "q" or user_entry[0]== "Q":
        break
    elif user_entry[0] in math_functions:
            if user_entry[0] =="+":
                result = add(user_entry[1], user_entry[2])
            elif user_entry[0] =="-":
                result = subtract(user_entry[1], user_entry[2])
            elif user_entry[0] =="*":
                result = multiply(user_entry[1],user_entry[2])
            elif user_entry[0] =="/":
                result = divide(user_entry[1], user_entry[2])
            elif user_entry[0] =="%":
                result = mod(user_entry[1],user_entry[2])
            elif user_entry[0] =="**2":
                result = square(user_entry[1])
            elif user_entry[0] =="**3":
                result = cube(user_entry[1])
            elif user_entry[0] =="**":
                result = power(user_entry[1], user_entry[2])
            print "The answer is %.2f" %(result)
    else:
        print "You didn't pick a valid math function."
        break