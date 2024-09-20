"""
    Let`s say you have a list of numbers and you want to return the
    five largest numbers or the five smallest numbers from that list.
    Normally, you can use the sorted() function and list slicing, but
    they only return a single number.
"""
def sort_list(arr: list):
    a = sorted(arr, reverse=True)
    return a[:5]

results = [102, 34, 67, 918, 90, 618, 55, 504, 614, 325]
print(sort_list(results))

"""
    This is cool, but slicing does not make code readable. There is a
    Python built-in module that you can use that will make your life
    easier. It is called heapq. With this module, we can easily return
    the 5 largest numbers using the nlargest method. The method
    takes two arguments: the iterable object and the number of
    numbers we want to return. Below, we pass 5, because we want
    to return the five largest numbers from the list.
"""
# Using nlargest
import heapq
results = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]
print(heapq.nlargest(5, results))

# Using nsmallest
import heapq
results = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]
print(heapq.nsmallest(5, results))