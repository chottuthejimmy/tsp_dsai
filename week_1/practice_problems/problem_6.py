'''
Problem 6: Patterns I
Write a function that takes in a number, and prints out a pattern.

If it's 3, you should print out,

* 
**
***
'''



def pattern_1(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()

pattern_1(3)

# def pattern_1_rec(n):   # Recursive solution
#     if n == 0:  
#         return
#     pattern_rec(n-1)
#     print('*' * n)

# pattern_1_rec(3)