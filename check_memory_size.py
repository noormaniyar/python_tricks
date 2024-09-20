"""
The sys module has a method that you can use for such a task.
Here is a code to demonstrate this. Given the same items, which
one is more memory efficient among a set, a tuple, and a list?
Let's use the sys module to find out.
"""

import sys
a = ['Love', 'Cold', 'Hot', 'Python']
b = {'Love', 'Cold', 'Hot', 'Python'}
c = ('Love', 'Cold', 'Hot', 'Python')
print(f'The memory size of a list is '
f'{sys.getsizeof(a)} ')
print(f'The memory size of a set is '
f'{sys.getsizeof(b)} ')
print(f'The memory size of a tuple is '
f'{sys.getsizeof(c)} ')