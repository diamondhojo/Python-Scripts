#Try to guess the number

import random

min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))
num = random.randint(min, max)

chance = round((min/max) * 100, 2)
print("The chances of you guessing correctly is " + str(chance) + "%")
guess = int(input("What's your guess? "))

if guess == num:
    print("You got it!")
else:
    print("Nope! Correct answer is " + str(f'{num:,}'))
