"""
    If you are working with large figures and you want to add a
    separator to make them more readable, you can use the format Q function.
"""

a = [10989767, 9876780, 9908763]
new_list =['{:,}'.format(num) for num in a]
print(new_list)


"""
    We can also use f-strings to add a thousand separators. Notice
    below that instead of using a comma (,) as a separator, we are
    using an underscore (_).
"""

a = [10989767, 9876780, 9908763]
new_list =[f"{num:_}" for num in a]
print(new_list)


