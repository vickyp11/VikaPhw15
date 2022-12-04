"""
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""
x = 5
def func_out():
    y = x + 5
    print("Outside function results in: ", y)
    def func_in():
        s = x**2
        print("Inside function results in: ", s)
    return func_in()

func_out()




