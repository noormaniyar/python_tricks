"""
    Set comprehension is similar to list comprehension; the only
    difference is that it returns a set and not a list. Instead of square
    brackets, set comprehension uses curly brackets. This is because
    sets are enclosed in curly brackets. You can use set comprehension
    on an iterable (list, tuple, set, etc.).
    Let`s say we have a list of uppercase strings and we want to convert
    them into lowercase strings and remove duplicates; we can use set
    comprehension. Since sets are not ordered, the order of the items
    in the iterable will be changed. Sets do not allow duplicates, so only
    one "PEACE" will be in the output set.
"""

list1 = ['LOVE', 'HATE', 'WAR', 'PEACE', 'PEACE']
set1 = {word.lower()for word in list1}
print(set1)

"""
    Here is another way we can use set comprehension. Let`s say we
    have a list of numbers and we want to return all the numbers from
    the list that are divisible by 2 and remove duplicates at the same
    time. Here is the code below: Remember, sets do not allow duplicates, 
    so it will remove all the numbers that appear more than once.
"""

arr = [10, 23, 30, 30, 40, 45, 50]
new_set = {num for num in arr if num % 2 == 0}
print(new_set)