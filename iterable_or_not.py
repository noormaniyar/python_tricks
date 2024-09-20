"""
    This is how you can use code to check if an item is iterable or
    not. We are using the iter() function. When you pass an item
    that is not iterable as an argument to the iter() function, it
    returns a TypeError. Below, we write a short script that checks
    if a given object is an iterable.
"""

arr = ['i' , 'love', 'working', 'with', 'Python']
try:
    iter_check = iter(arr)
except TypeError:
    print('object a not iterable')
else:
    print('object a is iterable')
# Check the second object
b = 45.7
try:
    iter_check = iter(b)
except TypeError:
    print('object b is not iterable')
else:
    print('object b is iterable')