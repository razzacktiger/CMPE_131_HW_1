import time 
def calculate_time(func):
    """ Decorater function which calculates the time taken for a function.
    Passes a function as an argument
    """
    def wrapper():
        Start_time = time.time()
        func()
        End_time = time.time()
        TimeTook = End_time - Start_time 
        print(f"Total time {TimeTook} ")
    return wrapper

@calculate_time
def some_func():
    """empty ucntion that takes 2 seconds to execute"""
    time.sleep(2)

some_func()


