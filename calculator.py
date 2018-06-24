"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# input from user
# split string by spaces (tokenize)

# check list[0] and compare to list of funtions(names or symbols)

# check number of operants with len(string.split)


while True:
    user_input = input(">>").split(" ")

    if len(user_input)<2:
        print ("Not enough inputs")
    elif len(user_input)>3:
        print ("Too many operands")
    elif len(user_input) == 2:
        num2=0
    else:
        num1=int(user_input[1])
        num2= int(user_input[2])

    if user_input[0] == "+":
        result = float(add_nums(num1,num2))
    elif user_input[0] == "-":
        result = float(subtract(num1, num2))
    elif user_input[0] == "*":
        result = float(multiply(num1, num2))
    elif user_input[0] == "/":
        result = float(divide(num1,num2))
    elif user_input[0] == "square":
        result = square(num1)
    elif user_input[0] == "cube":
        result = cube(num1)
    elif user_input[0] == "**":
        result = power(num1, num2)
    elif user_input[0] == "mod":
        result = mod(num1, num2)
    elif user_input[0]=="q" or user_input[0] == "quit":
        exit()
    else:
        print ("Sorry that wasn't clear, please try again")


