"""
    I will share with you three (3) ways you can flatten a list. The
    first method employs a for loop, the second employs the
    itertools module, and the third employs list comprehension.
"""

list1 = [[1, 2, 3],[4, 5, 6]]

# 1 = Using For Loop: 
newlist = []
for list2 in list1:
    for j in list2:
        newlist.append(j)
print(newlist, '--------new_list using forloop------')


# 2 = Using IterTools:
import itertools
flat_list = list(itertools.chain.from_iterable(list1))
print(flat_list, '---------flat list using itertools-------')


# 3 = Using List Comprehension
flat_list= [i for j in list1 for i in j]  # for j in list1, then for i in j , so the output will be i hence write i in the start.
print(flat_list, '----------flat_list using list comprehension----------')