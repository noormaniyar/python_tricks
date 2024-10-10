"""
    A generator is similar to a list comprehension, but instead of
    square brackets, you use parenthesis. Generators yield one item
    at a time, while list comprehension releases everything at once.
    Below, I compare list comprehension to a generator in two
    categories:
    1. Speed of execution.
    2. Memory allocation.
    Conclusion
    List comprehension executes much faster but takes up more
    memory. Generators execute a bit slower, but they take up less
    memory since they only yield one item at a time.
"""
import timeit
import sys
# function to check time execution
def timer(_, code):
    exc_time = timeit.timeit(code, number=1000)
    # return f'{_}: execution time is {exc_time:.2f}'
    return '{}: execution time is {:.2f}'.format(_, exc_time)

# function to check memory allocation
def memory_size(_, code):
    size = sys.getsizeof(code)
    # return f'{_}: allocated memory is {size}'
    return '{}: allocated memory is {}'.format(_, size)


one = 'Generator'
two = 'list comprehension'
print(timer(one, 'sum((num**2 for num in range(10000)))'))
print(timer(two, 'sum([num**2 for num in range(10000)])'))
print(memory_size(one,(num**2 for num in range(10000))))
print(memory_size(two,[num**2 for num in range(10000)]))
