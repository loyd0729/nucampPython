# Original code
"""
priceIsRight = 15

if priceIsRight:
    print("Price is too low!")
    if priceIsRight:
        print("Price is almost there!")
        if priceIsRight:
            print("Price is exactly that!")
        if priceIsRight:
            print("Price is too high!")
            
"""
priceIsRight = 15

if priceIsRight < 5:
    print("Price is too low!")
elif (priceIsRight >= 5) and (priceIsRight <= 9):
    print("Price is almost there!")
elif priceIsRight == 10:
    print("Price is exactly that!")
else:
    print("Price is too high!")