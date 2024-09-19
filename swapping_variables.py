"""
In python you can swap variables, once they have been assigned to objects.

In python we can also use XOR operator (exclusive or) to swap variables.This is a three step method, in the example below we are
swapping the values of x, y.
"""

x, y = 20, 30
x, y = y, x

print('x is : ', x)
print('y is : ', y)



x = 50
y = 60

x ^= y
y ^= x
x ^= y

# print('x is : ', x)
# print('y is : ', y)

print(f'x is : {x}')
print(f'y is : {y}')


