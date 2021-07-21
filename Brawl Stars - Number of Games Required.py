#Calculates the amount of games needed to unlock the next Trophy Road Goal

import math

trophies = int(input("How many trophies do you have? "))
required = int(input("How many trophies do you need total for the next Trophy Road Goal? "))
need = required - trophies
trophiesPerGame = 8

print("You need to wuin " + str(math.ceil(need/trophiesPerGame)) + " more games before unlcking the next Goal in Trophy Road")
