x = 0
while x < 10:
    x = x+1
    if x == 1:
        print("small")
    if x > 2:
        x = x+1
        print("medium")
    if x == 5:
        x = 7
        print("big")
        
while True: 
    print("True") 
    break 
    print("Break") 
    break 
    print("False") 

x = 3 
print(x) 
while True: 
    x = x - 1 
    if x == 1: 
        continue 
    elif x == 0: 
        print("END") 
        break 
    else: 
        print(x) 

print(1 > 3 or 2 > 1)

x = 1 + (0 * 10) * 3 / 8 ** 1
print(x)