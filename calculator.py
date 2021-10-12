import math
def calculator(number1, number2, operator):
    """Performs caluclations with *, **, /, //, %, -, +
    Takes in three arguments: "number1, number2, operator"
    returns result of operations 
    """
    if operator == '+':               
        result = number1 + number2
    if operator == '-':
        result = number1 - number2
    if operator == '*':
        result = number1 * number2
    if operator == '/':
        result = number1 / number2
    if operator == '//':
        if number2 == 0:
            return False 
        result = number1 // number2
    if operator == '**':
        result = number1 ** number2
    if operator == '%':
        result = number1 % number2
    return result 
def parse_input():
    """
    Takes in user inout and parses it into arguments which are passed into the calculator 
    """
    request = input("Enter Equation: ")
    arguments = request.split()
    if arguments[0].isdigit() and arguments[2].isdigit():
        arguments[0] = int(arguments[0])
        arguments[2] = int(arguments[2]) 
        print(calculator(arguments[0], arguments[2], arguments[1]))
    else:
        return False 





