"""
    When looping over an iterable, the print function prints each
    item on a new line. This is because the print function has a
    parameter called end. By default, the end parameter has an
    escape character (end = "\n"). Now, to print horizontally, we
    need to remove the escape character and replace it with an
    empty string (end =""). In the code below, take note of the space
    between the commas (""); this is to ensure that the numbers are
    printed with spaces between them. If we remove the space (""),
    the numbers will be printed like this: 1367

    The print function has another parameter called sep. We use
    sep to specify how the output is separated.
"""

print("1", "2", "3", sep="/")



list1 = [1, 3, 6, 7]
for num in list1:
    print(num, end=" ")


