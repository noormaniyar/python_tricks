"""
    We can use the assert statement to check or debug your code. The
    assert statement will catch errors early on in the code. The assert
    statement takes two arguments: a condition and an optional
    error message. Here is the syntax below:

    assert <conditions [error message]
    
    The condition returns a Boolean value of either True or False. The
    error message is the message we want to be displayed if the condition is False.

    Below, we insert an assert statement in the code. This code takes
    a list of names and returns all the names in lowercase letters. We
    expect all the items in the list to be strings, so we use the insert
    statement to debug for non-string entries. The insert statement
    will check if all the items in the list are of type str. If one of the
    items is not a string, it will evaluate to False. It will halt the
    program and throw an AssertionError. It will display the error
    message that "non-string items are in the list." 
    If all the items are strings, it will evaluate to True and run the rest of the
    code. The code returns an error because the fourth name in the
    list of names is not a string.
"""

name = ["Jon","kelly", "kess", "PETR", 4]
lower_names = []
for item in name:
    assert type(item) == str, 'non-string items in the list-------'
    if item.islower() :
        lower_names.append(item)
print(lower_names)

"""
    If we remove the non-string item from the list, the rest of the
    code runs.
"""

name = ["Jon","kelly", "kess", "PETR"]
lower_names = []
for item in name:
    assert type(item) == str, 'non-string items in the list'
    if item.islower():
        lower_names.append(item)
print(lower_names)