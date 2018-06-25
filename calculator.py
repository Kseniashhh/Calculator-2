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

    if "q" in user_input:
        print ("Sad you're leaving")
        break

    if user_input[0] not in ['+','-','*','/','**','square','mod','cube']:
        print ("Sorry that wasn't clear, please try again")
    else:
        if len(user_input)<2:
            print ("Not enough inputs")
            continue
        elif len(user_input)>3:
            print ("Too many operands, try again")
            continue
        elif user_input[1].isdigit():
            if len(user_input) == 2:
                num1=int(user_input[1])
                num2=0
            else:
                num1=int(user_input[1])
                num2= int(user_input[2])

        if user_input[0] == "+":
            result = float(add(num1,num2))
        elif user_input[0] == "-":
            result = float(subtract(num1, num2))
        elif user_input[0] == "*":
            result = float(multiply(num1, num2))
        elif user_input[0] == "/":

            result = divide(num1,num2)
            if result is not None:
                result = float(result)
            else:
                result = "Try again"
        elif user_input[0] == "square":
            result = square(float(num1))
        elif user_input[0] == "cube":
            result = cube(float(num1))
        elif user_input[0] == "**":
            result = power(float(num1),float(num2))
        elif user_input[0] == "mod":
            result = mod(float(num1), float(num2))
        # else:
        #     False
        print(result)


