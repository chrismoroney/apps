import math
import random

pity = 0

def pull_one():
    global pity
    pity += 1
    if pity == four_star_pity:
        print(4)
        new_four_star()
    elif pity == five_star_pity:
        print(5)
        pity = 0
        new_five_star()
    else:
        print(3)

def pull_ten():
    for i in range(10):
        pull_one()

def first_four_star():
    return random.randrange(1, 10)

def first_five_star():
    num = random.randrange(1, 90)
    while four_star_pity == num:
            num = random.randrange(1, 90)
            print("Four star pity: " + num)
    return num

def new_four_star():
    num = random.randrange(1, 10)
    while four_star_pity == five_star_pity:
        num = random.randrange(1, 10)
        print("Four star pity: " + num)
    return num
    

def new_five_star():
    while five_star_pity == four_star_pity:
        num = random.randrange(1, 90)
        print("Five star pity: " + num)
    return num

still_pulling = True

four_star_pity = first_four_star()
five_star_pity = first_five_star()

print(four_star_pity)
print(five_star_pity)

while still_pulling:

    command = str(input("Please enter 1 or 10: "))

    if command == "1":
        pull_one()
    elif command == "10":
        pull_ten()
    else:
        still_pulling = False
        