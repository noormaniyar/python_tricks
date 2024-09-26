"""
    When you are not sure how many arguments you will need for
    your function, you can pass *args (non-keyword arguments) as a
    parameter. The * notation tells Python that you are not sure how
    many arguments you need, and Python allows you to pass in as
    many arguments as you want. Below, we calculate the average
    with different numbers of arguments. First, we pass three (3)
    numbers as arguments. Then we pass six numbers as arguments.
    The *args make functions more flexible when it comes to arguments.
"""

def avg(*args):
    avg1 = sum(args)/len(args)
    return f'The average is {avg1:.2f}'
print(avg(12, 34, 56))
print(avg(23,45,36,41,25,25))

"""
    When you see **kwargs (keyword arguments) as a parameter, it
    means the function can accept any number of arguments as a
    dictionary (arguments must be in key-value pairs).
"""

def myFunc(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')
        # print('\n')
myFunc(Name = 'Ben',Age = 80, Occupation ='Engineer')