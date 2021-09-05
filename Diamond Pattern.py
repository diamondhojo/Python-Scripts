
import math

size = 13 #maximum number of * at it's widest line (must be odd number)
stars = 1
spaces = size-stars
half = "first"

for i in range(size):
    print((" " * int(spaces/2)) + ("*" * int(stars)) + (" " * int(spaces/2)))
    
    if(half == "first"):
        stars = stars+2
        spaces = size-stars
        if(stars > size):
            half = "second"
            stars = stars-2
            spaces = 0
            
    if(half == "second"):
        stars = stars-2
        spaces = spaces+2
        if(stars < 1):
            break
