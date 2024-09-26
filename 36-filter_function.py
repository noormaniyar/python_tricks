"""
    We can use the filter() function as an alternative to the for loop.
    If you want to return items from an iterable that match certain
    criteria, you can use the Python filter() function.
    Let`s say we have a list of names and we want to return a list of
    names that are lowercase; here is how you can do it using the
    filter() function.
"""

# Example 1: Using a for loop

names = ['Derick', 'John', 'moses', 'linda']
lower_case = []
for name in names:
    if name.islower() :
        lower_case.append(name)
print(lower_case)



# Example 2: Using filter function with lambda function

"""
    The filter() function is a higher-order function. The filter
    function takes two arguments: a function and a sequence. It uses
    the function to filter the sequence. In the code below, the filter
    function uses the lambda function to check for names in the list
    that are lowercase.
"""
names = ['Derick', 'John', 'moses', 'linda']
lowercase_lambda = list(filter(lambda x:x.islower(), names))
print(lowercase_lambda)



# Example 3: Using filter function with a function

"""
    If we do not want to use a lambda function, we can write a
    function and pass it as an argument to the filter function.
"""

names = ['Derick', 'John', 'moses', 'linda']

def lower_names(n):
    return n.islower()
filter_lower_case = list(filter(lower_names, names))
print(filter_lower_case)