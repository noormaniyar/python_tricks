"""
If you want to know how many times item appears in an iterable, you can use the counter() class from the collection module.
The counter() class will return a dictionary of how many times each item appears in an iterable.

Let`s say we want to know how many times the name Peter appears in the following list;
here is how we can use the counterQ class of the collections module. 
"""

from collections import Counter

list1 = ['John','Kelly', 'John', 'Moses', 'John']
count_peter = Counter(list1).get("John")
print(f'The name John appears in the list is : {count_peter} times.')


"""
Another way you can do it is by using a normal for loop. This is the naive way.
"""


list2 = ['John','Kelly', 'Peter', 'Moses', 'Peter']
count = 0
for name in list2:
    if name == 'Peter':
        count +=1
print(f'The name Peter appears in the list : , {count} times.')

