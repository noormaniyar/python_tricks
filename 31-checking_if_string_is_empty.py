"""
    The simple way to check if a given string is empty is to use the
    if statement and the not operator, which will return a Boolean
    value. Empty strings in Python evaluate to False, and strings
    that are not empty evaluate to True. The not operator returns
    True if something is False and False if something is True. Since
    an empty string evaluates to False, the not operator will return
    True. Below, if a string is empty, the if statement will evaluate
    to True, so that part of the code will run. If a string is not empty,
    the else statement will run.
"""

# Empty string
strl = ''
if not strl:
    print(f'This string is empty')
else:
    print(f'This string is NOT empty')

# Not empty string
str2 = 'string'
if not str2:
    print(f'This string is empty')
else:
    print(f'This string is NOT empty')