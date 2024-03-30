'''
Problem 8: Word Frequency
Write a function that takes in a string as a function and returns a dictionary of alphabet frequency in the string. Your function should ignore all characters apart from English uppercase and lowercase alphabets.

For instance, my_func("Hello World! 123") should return {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}.

'''

def word_frequency(s):
    s = s.lower()
    freq = {}
    for char in s:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1  # 0 is mentioned to return 0 if the key is not present in the dictionary. If not mentioned, it will return None. and None + 1 will throw an error.
    return freq

print(word_frequency("Hello World! 123"))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}