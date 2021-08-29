import random

number = []

while len(number) < 6:
number.append(random.randint(1,100))

set_number = set(number)

while len(set_number) != len(number):
    x = random.randint(1,100)

    if x in set_number:
        pass
    else:
        set_number = list(number)
        set_number.append(x)
    
    
print (set_number, /n "Edited with VIM")
