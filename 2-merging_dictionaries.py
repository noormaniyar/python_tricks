"""
    If you have two dictionaries that you want to combine, you can
    do so using two easy methods. You can use the merge ( | )
    operator or the (**) operator. Below, we have two dictionaries,
    a and b. We are going to use these two methods to combine the
    dictionaries
"""

# Method 1
# Using the merge ( | ) operator.

name1 = {"kelly": 23, "Derick": 14}
name2 = {"Ravi": 45, "Mpho": 67}

# names = name1 | name2   # this line of code will work for python version above 3.9
# print(names)



# Method 2
# Using the update method. With this method, you need to

name1 = {"Ronak": 23, "Soham": 14}
name2 = {"Rekha": 45, "Ruby": 67, "Rajni": 45, "Rutuja":66}

name1.update(name2)
print(name1)

# or

merged_names = name1.copy()  # Create a copy to avoid modifying the original
merged_names.update(name2)
print(merged_names)



# Method 3
# Using the merge ( ** ) operator. With this operator, you need to

name1 = {"abraham" : 23, "ziyan": 14, "Rahul": 7}
name2 = {"Rohit": 45, "Raj": 67}
names = {**name1, **name2}
print(names)