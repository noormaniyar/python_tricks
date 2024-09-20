"""
    You have two strings; how would you go about checking if they
    are anagrams?
    If you want to check if two strings are anagrams, you can use
    counterQ from the collections module. The counterQ supports
    equality tests. We can basically use it to check if the given
    objects are equal. In the code below, we are checking if a and b
    are anagrams.
"""

from collections import Counter
a = 'lost'
b = 'stol'
print(Counter(a)==Counter(b))

"""
    We can also use the sortedQ function to check if two strings
    are anagrams. By default, the sortedQ function will sort a
    given string in ascending order. So, when we pass strings as
    arguments to the sorted function for equality tests, first the
    strings are sorted, then compared. See the code below:
"""

a = 'lost'
b = 'stol'
if sorted(a)== sorted(b):
    print('Anagrams')
else:
    print("Not anagrams")