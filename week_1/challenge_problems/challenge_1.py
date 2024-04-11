'''
Challenge 1: Compute 1000!
In one of the problems in the previous section, you were asked to write a function that computes the factorial of a number. However, that function is only good for relatively small numbers. Factorials have a tendency to grow extremely rapidly such even 20! is more than 2 billion billion!

Even the most powerful supercomputer in the world will not be able to compute 1000! the normal way. The number is enormous; it has close to 2500 digits!

Your first challenge is to figure out a clever way to compute this number anyway.

Hint: If you had to compute this by hand, it wouldn't be that difficult. You would probably need a few hours and a really, really long piece of paper. Can you write a program that mimics multiplication by hand?

'''

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(1000))


