"""
    Below are three different ways you can access the keys of a dictionary.
"""

# 1. Using set comprehension
# Set comprehension is similar to list comprehension. The
# difference is that it returns a set.
dict1 = {'name': 'Mary', 'age': 22, 'student':True, 'Country': 'UAE'}
print({key for key in dict1.keys()})


# 2. Using the set() function
dict1 = {'name': 'Mary', 'age': 22, 'student':True, 'Country': 'UAE'}
print(set(dict1))


# 3. Using the sorted() function
dict1 = {'name': 'Mary', 'age': 22, 'student':True, 'Country': 'UAE'}
print(sorted(dict1))