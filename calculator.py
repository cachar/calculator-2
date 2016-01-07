"""
calculator.py

Using our arithmetic.py file from Euser_entryercise02, create the
calculator program yourself in this file.
"""

from arithmetic_2 import *

integer_nums =[]

def integerizing(numbers): 
    """We are turning a list of strings into a list of integers"""  

    for num in numbers:
        try:
            integer_nums.append(int(num))
        except ValueError:
            print "You need to type numbers, please."
    #print integer_nums
    #return integer_nums

def new_game():
    """Starting a new game, with everything that involves, with arithmetic.py"""
    
    user_entry = raw_input("Please type an arithmetic function followed by any numbers separated by spaces. ")
    response = user_entry.split(" ")
    numbers = response[1:]
    integerizing(numbers)
    if len(integer_nums) < 2:
        print "You didn't enter at least 2 numbers. Try again."
        new_game()

    #print response[0]
    #print integer_nums

    if response[0] == "q" or response[0]== "Q":
        print "Bye!"
    elif response[0] =="+" or response[0] == "add":
        result = add(integer_nums)
    elif response[0] =="-" or response[0] == "subtract":
        result = subtract(integer_nums)
    elif response[0] =="*" or response[0] == "multiply":
        result = multiply(integer_nums)
    elif response[0] =="/" or response[0] == "divide":
        result = divide(integer_nums)
    elif response[0] =="%" or response[0] == "mod":
        result = mod(integer_nums)
    elif response[0] =="**2" or response[0] == "square":
        result = square(integer_nums)
    elif response[0] =="**3" or response[0] == "cube":
        result = cube(integer_nums)
    elif response[0] =="**" or response[0] == "pow":
        result = power(integer_nums)
    else:
        print "You didn't pick a valid math function."
        new_game()
    print "Your result is %.2f" % (result)
new_game()