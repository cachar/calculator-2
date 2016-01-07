"""
calculator.py

Using our arithmetic.py file from Euser_entryercise02, create the
calculator program yourself in this file.
"""

from arithmetic_2 import *
user_entry = raw_input("Please type an arithmetic function followed by any numbers separated by spaces. ")
# Your code goes here
def integerizing(numbers): 
    """We are turning a list of strings into a list of integers"""  
    integer_nums =[]
    for num in numbers:
        integer_nums.append(int(num))
    print integer_nums
    return integer_nums

while True:

    response = user_entry.split(" ")
    numbers = response[1:]

    integerizing(numbers)
    if response[0] == "q" or response[0]== "Q":
        break
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
        print "The answer is %.2f" %(result)
        break
    else:
        print "You didn't pick a valid math function."