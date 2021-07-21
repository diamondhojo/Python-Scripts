
import random
import math
import msvcrt

snakes = []
ladders = []
p1 = 0
p2 = 0
turn = "p1"
winner = ""

for i in range(10):
    snakes.append(random.randint(30, 100))

for i in range(10):
    num = random.randint(1, 70)
    if(num not in snakes):
        ladders.append(num)
    else:
        print("Crossover")
print(snakes)
print(ladders)

while (winner == ""):
    if (turn == "p1"):
        input("\nPlayer 1, press Enter to roll.")
        roll =  random.randint(1, 6)
        p1 = p1 + roll
        print("Roll: +" + str(roll))
        if (p1 in ladders):
            amount = random.randint(10, 30)
            p1 = p1 + amount
            print("Ladder! +" + str(amount) + " points!")
        elif(p1 in snakes):
            amount = random.randint(10, 30)
            if((p1 - amount) < 0):
                p1 = 0
            else:
                p1 = p1 - amount
            print("Snake! -" + str(amount) + " points!")
        print("Player 1: " + str(p1))
        if(p1 >= 100):
            print("Congradulations, Player 1!")
            break
        turn = "p2"
    elif (turn == "p2"):
        input("\nPlayer 2, press Enter to roll.")
        roll =  random.randint(1, 6)
        p2 = p2 + roll

        print("Roll: +" + str(roll))
        if (p2 in ladders):
            amount = random.randint(10, 30)
            p2 = p2 + amount
            print("Ladder! +" + str(amount) + " points!")
        elif(p2 in snakes):
            amount = random.randint(10, 30)
            if((p2 - amount) < 0):
                p2 = 0
            else:
                p2 = p2 - amount
            print("Snake! -" + str(amount) + " points!")
        print("Player 2: " + str(p2))
        if(p2 >= 100):
            print("Congradulations, Player 2!")
            break
        turn = "p1"
