"""
    You can sort a list of tuples using the itemgetter() class of the
    operator module. The itemgetter() function is passed as a key
    to the sorted() function. If you want to sort by the first name,
    you pass the index (0) to the itemgetter() function. Below are
    different ways you can use itemgetter() to sort the list of tuples.
"""

from operator import itemgetter
names = [('Ben','Jones'),('Peter','Parker'),('Kelly','Isa')]

#Sort names by first name
sorted_names = sorted(names,key=itemgetter(0))
print('Sorted by first name',sorted_names)

# sort names by last name
sorted_names = sorted(names,key=itemgetter(1))
print('Sorted by last name',sorted_names)

# sort names by first name, then last name
sorted_names = sorted(names,key=itemgetter(0,1))
print('Sorted by last name & first name',sorted_names)