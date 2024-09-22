"""
    The type() function is usually used to check the type of an object.
    However, it can also be used to create classes dynamically in Python.
    Below I have created two classes, the first one using the class
    keyword and the second one using the type() function. You can
    see that both methods achieve the same results.
"""
# Creating dynamic class using the class keyword
class Car:
    def __init__ (self, name, color):
        self.name = name
        self.color = color
    def print_car(self):
        return f'The car is {self.name} and its {self.color} in color'
carl = Car('BMW', 'Green')
print(carl.print_car())

# Creating dynamic class using the type keyword
# def cars_init(self, name ,color):
#     self.name = name
#     self.color = color
# Cars = type("Car" , () ,
# {'__init__ ': cars_init,
# 'print_car':lambda self:
# f'The car is {self.name} '
# f'and its {self.color} in color'})
# carl = Cars("BMW", "Green")
# print(carl.print_car())