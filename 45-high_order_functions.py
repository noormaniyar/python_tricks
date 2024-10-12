"""
    A high-order function is a function that takes another function
    as an argument or returns another function. The code below
    demonstrates how we can create a function and use it inside a
    high-order function. We create a function called sort names,
    and we use it as a key inside the sortedQ function. By using
    indexfo], we are basically telling the sorted function to sort
    names by their first name. If we use [1], then the names would
    be sorted by the last name.
"""

def sort_names(x):
    return x[0]
names = [('John','Kelly') , ('Chris','Rock') , ('will',' smi tn') ]
sorted_names = sorted(names, key= sort_names)
print(sorted_names)

"""
    If we don’t want to write a function as above, we can also use
    the lambda function. See below:
"""

names = [('JohnKelly'), ('ChrisRock'), ('wi11','Smith')]
sorted_names = sorted(names, key= lambda x: x[0])
print(sorted_names)