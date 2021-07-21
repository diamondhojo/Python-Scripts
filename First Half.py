"""
First Half
https://codingbat.com/prob/p107010

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""
def first_half(string):
    if (int(len(string).real/2) % 2) == 0:
        leftHalf = len(string).real/2
        print(string[:int(leftHalf)]) #Pseudo Code --> print(string[:2])
    else:
        print("Please enter an even number")

first_half(input("Enter a single word: "))