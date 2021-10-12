import math
def calculator(number1, number2, operator):
    if number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number1)
    else:
        return False
    if operator == '+':               
        result = number1 + number2
    if operator == '-':
        result = number1 - number2
    if operator == '*':
        result = number1 * number2
    if operator == '/':
        result = number1 / number2
    if operator == '//':
        result = number1 // number2
    if operator == '**':
        result = number1 ** number2
    if operator == '%':
        result = number1 % number2
    return result 
def parse_input():
    request = input("Enter Equation: ")
    arguments = request.split()
    print(calculator(arguments[0], arguments[2], arguments[1]))

parse_input()




