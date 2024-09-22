"""
    The simplest way to access the index of items in an iterable is by
    using the enumerate() function. By default, the enumerate
    function returns the element and its index. We can basically use
    it to loop over an iterable, and it will return a counter of all the
    elements in the iterable.
    Let`s say we want to find the index of the letter "n" in stn below.
    Here is how we can use the enumerate function to achieve that:
"""
str1 = 'string'
for index, value in enumerate(str1):
    if value =='n' :
        print(f"The index of n is {index}")


"""
    If we want to print all the elements in the string and their indexes, 
    here is how we can use enumerate.
"""
str1 = 'string'
for i , j in enumerate(str1):
    print(f"Index: {i}, Value: {j}")

"""
    If you don`t want to use a for loop, you can use enumerate with
    the list function, and it will return a list of tuples. Each tuple will
    have a value and its index.
"""
strl = 'string'
str_counta = list(enumerate(strl))
print(str_counta)