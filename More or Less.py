#Enter min and max values, try to guess if the second number is greater than, equal to, or less than the first number

import random
import time

min = int(input("Enter your minimum number: "))
max = int(input("Enter your maximum number: "))

first = random.randint(min,max)
second = random.randint(min,max)

print ("The first number is " + str(first))
choice = input("Do you think the second number will be higher, lower, or the same as the first number? ")

if choice == "higher" or choice =="lower" or choice == "same":
    if choice == "higher" and second > first:
        print ("You're correct")
    elif choice == "lower" and first > second:
        print("You're correct")
    elif choice == "same" and first == second:
        print("You're correct")
    else:
        print("You're wrong")
        time.sleep(1)
        print("Idiot.")
        time.sleep(1)
else:
    print("Answer with 'higher', 'lower', or 'same'")
