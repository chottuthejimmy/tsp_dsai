'''
Problem 2: Add n numbers
Now, write a function that takes in an arbitrary number of arguments and returns their sum.
For instance, my_func(2, 3) would return 5, my_func(5, 1, 4) would return 10, and so on.
Hint: Google *args in Python and what they can do.
'''

def add_n_numbers(*args):  # *args is a tuple of arguments
    return sum(args)

print(add_n_numbers(2, 3)) # 5
print(add_n_numbers(5, 1, 4)) # 10