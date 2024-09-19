"""
    Using the enumerate Q, max(), and min() functions, we can find
    the index of the biggest and the smallest number in a list. The
    max function is a high-order function; it takes another function
    as an argument.
    In the code below, the max() function takes the list and the
    lambda function as arguments. We add the enumerate^
    function to the list so it can return both the number in the list
    and its index (a tuple). We set the count in the enumerate
    function to start at position zero (o). The lambda function tells
    the function to return a tuple pair of the maximum number and its index.
"""

# Find the index of the largest number
x = [12, 45, 67, 89, 34, 67, 13]
max_num = max(enumerate(x, start=0), key = lambda x: x[1])
print('The index of the largest number is', max_num[0])


# Find the index of the smallest number
x = [12, 45, 67, 89, 34, 67, 13]
min_num = min(enumerate(x, start=0), key = lambda x : x[1])
print('The index of the smallest number is', min_num[0])