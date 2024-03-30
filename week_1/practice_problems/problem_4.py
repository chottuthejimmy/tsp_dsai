'''
Problem 4: Temperature converter
Write a function that converts celsius to fahrenheit, and vice versa.

The formulae are as follows:
Fahrenheit to Celsius: (F - 32) * 5/9
Celsius to Fahrenheit: (C * 9/5) + 32

Your function should take 2 arguments: a temperature and the scale the temperature needs to be converted to.
For instance, my_func(100, 'F') would assume that 100 is in Celsius and would convert it to 212F (in other words, it would return 212). On the other hand my_func(100, 'C') would assume 100 is in Fahrenheir and would convert it to 37.7C.
You can assume that the second argument of your function will always be either C or F.
'''

def temp_converter(temp, scale):
    if scale is 'F':
        return round((temp * 9/5) + 32, 2)
    return round((temp - 32) * 5/9, 2)

print(temp_converter(100, 'F')) # 212
print(temp_converter(100, 'C')) # 37.78
