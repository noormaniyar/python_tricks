"""
    Let`s say you have a string and you want to find the most
    frequent element in the string; you can use the max() function.
    The max() function will count the items in the string and return
    the item that appears the most. You just have to pass the string
    count method to the key parameter. Let`s use the string below
    to demonstrate this
"""

a = 'fecklessness'
most_frequent = max(a, key = a.count)
print(f'The most frequent letter is, 'f'{most_frequent}')


"""
    Now, if there is more than one most frequent item in the string,
    the max() function will return the element that comes first
    alphabetically. For example, if the string above had 4 Fs and 4 Ss,
    the max function would return "f" instead of "s" as the most
    frequent element because "f" comes first alphabetically.
    We can also use the Counter class from the collections module.
    The most_common() method of this class will count how many
    times each element appears in the list, and it will return all the
    elements and their counts, as a list of tuples. Below, we pass the
    parameter (1) because we want it to return the number one most
    common element of the list. If we pass (2), it will return the two
    most common elements.
"""

import collections
a = 'fecklessness'
print(collections.Counter(a).most_common(1))