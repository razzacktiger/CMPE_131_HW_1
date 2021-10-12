import time 
def tripler(func):
    """ Decorater function which calculates the time taken for a function.
    Passes a function as an argument
    """
    def wrapper(): 
        func()
        func()
        func()
    return wrapper

@tripler
def function():
    """prints triple"""
    print('triple')
