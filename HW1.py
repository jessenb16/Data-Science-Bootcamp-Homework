# Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
"""
def count_vowels(word):
    count = 0
    vowels = {'a','e','i','o','u'}
    for char in word.lower():
        if char in vowels:
            count += 1 
    return count

word1 = "Hello"
word2 = "Flrf"
word3 = "EEEeee"

print(count_vowels(word1))
print(count_vowels(word2))
print(count_vowels(word3))

"""
#Iterate through the following list of animals and print each one in all caps.

"""
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())
"""
#Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
"""
for int in range(21):
    if int % 2 == 0:
        print(f"{int} is even.")
    else:
        print(f"{int} is odd.")
"""

#Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
"""
def sum_of_integers(a,b):
    return a + b

print(sum_of_integers(-30,4))
"""