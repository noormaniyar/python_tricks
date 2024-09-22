"""
    Since enumerate counts (adds a counter) the items it loops over,
    you can use it to create a list of tuples. Below, we create a list of
    tuples of days in a week from a list of days. Enumerate has a
    parameter called "start." Start is the index at which you want
    the count to begin. By default, the start is zero (o).
    Below, we have set the start parameter to one (1). You can start
    with any number you want.
"""
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_tuples = list(enumerate(days, start=1))
print(days_tuples)


"""
    It is also possible to create the same output with a for loop.
    Let`s create a function to demonstrate this.
"""
def enumerate(days, start= 1):
    n = start
    for day in days:
        yield n, day
    n += 1
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(list(enumerate(days)))