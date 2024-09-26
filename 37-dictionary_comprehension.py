"""
    Dictionary comprehension is a one-line code that transforms a
    dictionary into another dictionary with modified values. It makes
    your code intuitive and concise. It is similar to list comprehension.
    Let`s say you want to update the values of the dictionary from
    integers to floats; you can use dictionary comprehension. Below,
    k accesses the dictionary keys, and v accesses the dictionary values.
"""

dict1 = {'Grade': 70, 'Weight': 45, 'Width': 89}
# Converting diet values into floats
dict2 = {k: float(v) for (k, v) in dict1.items()}
print(dict2)


"""
    Let`s say we want to divide all the values in the dictionary by 2;
    here is how we do it.
"""

dictl = {'Grade': 70, 'Weight': 45, 'Width': 89}
# dividing diet values by 2
dict2 = {k: v/2 for (k, v) in dictl.items()}
print(dict2)