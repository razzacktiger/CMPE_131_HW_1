import math
def calculator(number1, number2, operator):
    """Performs """
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
    """
    takes in user inout and parses it into arguments which are passed into the calculator 
    """
    request = input("Enter Equation: ")
    arguments = request.split()
    print(calculator(arguments[0], arguments[2], arguments[1]))





