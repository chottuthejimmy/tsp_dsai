'''
Problem 5: List Manipulation
Write a function that takes in a list of numbers as input and performs the following operations sequentially:

Remove all odd numbers
Double every remaining number
Sum all the modified numbers
There is one caveat here though: you're not allowed to use loops! If you feel like you don't know how to proceed, maybe googling List Comprehension in Python might help :)

As an example, my_func([1, 2, 3, 4, 5]) would remove all odd numbers to create [2, 4], double the numbers to create [4, 8] and then return a final answer of 12.
'''

def list_manipulation(lst):
     return sum([num * 2 for num in lst if num % 2 == 0])

lst = [1, 2, 3, 4, 5]
print(list_manipulation(lst)) # 12