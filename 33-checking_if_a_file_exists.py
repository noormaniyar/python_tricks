"""
    Using the OS module, you can check if a file exists. The os module
    has an exists() function from the path() class that returns a
    Boolean value. If a file exists, it will return True; if not, it will
    return False. When working with files, it is important to check if
    a file exists before trying to run it to avoid generating errors. Let's
    say you want to delete or remove a file with Python; if the file does
    not exist, your code will generate an error
"""
# import os
# os.remove("thisfile.txt")


"""
    To avoid this error, we have to check if the file exists before
    removing it. We will pass the file path or file name as an
    argument to os.path.exists(). If the file is in the same folder as your
    Python file, we can pass the file name as an argument.
    In the code below, we use the file name as an argument because
    we assume the file is in the same folder as the Python file. You
    can see from the output that even though the file does not exist,
    our code does not generate an error.
"""

import os.path
file = os.path.exists('thisfile.txt')
print(file, '--------file=======')
if file:
    print(file, '---------file----------')
    os.remove("thisfile.txt")
else:
    print('This file does Not exist')