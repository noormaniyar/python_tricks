"""
    Do you understand the distinction between a return statement
    and a yield statement in a function? The return statement returns
    one element and ends the function. The yield statement returns
    a "package" of elements called a generator. You have to "unpack"
    the package to get the elements. You can use a for loop or the
    next() function to unpack the generator.
"""

# Example 1: Using return statement
def num (n: int) -> int:
    for i in range(n):
        return i
    print(num(5))

"""
    You can see from the output that once the function returns o, it
    stops. It does not return all the numbers in the range.
"""


# Example 2: Using yield
def num (n: int):
    for i in range(n):
        yield i
# creating a generator
gen = num(5)
#unpacking generator
for i in gen:
    print(i, end = '')

"""
    The yield function returns a "package" of all the numbers in the
    range. We use zfor loop to access the items in the range.
"""