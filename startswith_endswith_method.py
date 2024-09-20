"""
    The startswith () and endswith () are string methods that return
    True if a specified string starts with or ends with a specified value.
    Let`s say you want to return all the names in a list that start with "a" and ends with "e"; 
    here is how you would use startswith () to accomplish that.
"""

# Using startswith()

list1 = ['lemon','Orange','apple', 'apricot']
new_list = [i for i in list1 if i.startswith('a')]
print('New List which starts with a is: ', new_list)

# Using endswith()

list1 = ['lemon','Orange','apple', 'apricot']
new_list = [i for i in list1 if i.endswith('e')]
print('New List which ends with e is: ', new_list)
