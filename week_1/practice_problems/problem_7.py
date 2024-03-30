'''
Problem 6: Patterns II
Write a function that takes in a number, and prints out a mirror pattern of the last one.

If it's 3, you should print out,

  *
 **
***
'''

def pattern_2(n):
    space = n - 1
    for i in range(n):
        for j in range(space):
            print(' ', end='')
        for k in range(i+1):
            print('*', end='')
        print()
        space -= 1

pattern_2(3)

# def pattern_2_rec(n, level=1):  # Recursive solution
#     if level > n:
#         return
#     print(' ' * (n - level) + '*' * level)
#     pattern_2_rec(n, level + 1)

# pattern_2_rec(3)