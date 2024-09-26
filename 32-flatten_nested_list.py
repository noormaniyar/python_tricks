# Using sum function
"""
    What is a nested list? A nested list is a list that has another list as
    an element (a list inside a list). You can flatten a nested list using
    the sum() function. Note that this will work on a two-dimensional nested list.
"""

nested_list1 = [[2, 4, 6],[8, 10, 12]]
new_list1 = sum(nested_list1,[])
print(new_list1)


# Using reduce function
"""
    Here is another cool trick you can use to flatten a two-dimensional
    list. This time we use reduce from functools module. This is
    another high order function in Python.
"""

from functools import reduce
nested_list2 = [[2, 4, 6], [8, 10, 12]]
new_list2 = reduce(lambda x, y: x+y, nested_list2)
print(new_list2)