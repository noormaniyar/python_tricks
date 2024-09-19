"""
    The sort() method will sort a list in ascending order (by default).
    For the sort method to work, the list should have the same type
    of objects. You cannot sort a list mixed with different data types,
    such as integers and strings. The sort() method has a parameter
    called reverse; to sort a list in descending order, set reverse to
    True.
"""


list1 = [2, 5, 6, 8, 1, 8, 9, 11]
list1.sort(reverse=True)
print(list1, '---------list1 with descending order------')

"""
    Remember, sort() is strictly a list method. You cannot use it to
    sort a set, a tuple, a string, or a dictionary.
    The sort() method does not return a new list; it sorts an existing
    list. If you try to create a new object using the sort() method, it
    will return None. See below:
"""

list1 = [2, 5, 6, 8, 1, 8, 9, 11]
list2 = list1.sort(reverse=True)
print(list1, '-------list1 with descending order------')
print(list2, '--------new list--------')
