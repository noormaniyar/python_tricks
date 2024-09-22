"""
    The sorted() function is a high-order function because it takes
    another function as a parameter. Here, we create a lambda
    function that is then passed as an argument to the sorted()
    function key parameter. By using a negative index [-1], we are
    telling the sorted() function to sort the list in descending order.
"""

listl = ['Mary', 'Peter', 'Kelly']
a = lambda x: x[-1]
y = sorted(listl, key=a)
print('Ascending sorted list is : ', y)

"""
    To sort the list in ascending order, we can just change the
    index to [: 1]. See below:
"""

listl = ['Mary', 'Peter', 'Kelly']
a = lambda x: x[:1]
y = sorted(listl, key=a)
print('Descending sorted list is : ', y)

"""
    Another easy way to sort the list in ascending order would be
    to use just the sorted() function. By default, it sorts an iterable
    in ascending order. Since the key parameter is optional, we
    just leave it out.
"""

listl = ['Mary', 'Peter', 'Kelly']
list2 = sorted(listl)
print('Ascending sorted list is : ', list2)