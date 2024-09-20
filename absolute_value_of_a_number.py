"""
    Let`s say you have a negative number and you want to return
    the absolute value of that number; you can use the abs()
    function. The Python abs() function is used to return the
    absolute value of any number (positive, negative, and complex
    numbers). Below, we demonstrate how we can return a list of
    absolute numbers from a list of numbers that have negative and
    positive numbers.
"""

# for list , Using list comprehension.

list1 = [-12, -45, -67, -89, -34, 67, -13]
print('Absolut No of a list is: ', [abs(num) for num in list1])


# for floating number.

a = -23.43
print('Absolute No of Floating No is: ', abs(a))


# for complex number.

complex_num = 6 + 3j
print('Absolute No of Complex No is: ', abs(complex_num))