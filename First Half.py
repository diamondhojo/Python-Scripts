"""
First Half
https://codingbat.com/prob/p107010

Give a string of even length, this returns the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
"""

def first_half(string):
    if (int(len(string)) % 2) == 0:
        leftHalf = len(string).real/2
        print(string[:int(leftHalf)]) #Pseudo Code --> print(string[:2])
    else:
        first_half(input("Enter a single word w/ even number of characters: "))

first_half(input("Enter a single word w/ even number of characters: "))
