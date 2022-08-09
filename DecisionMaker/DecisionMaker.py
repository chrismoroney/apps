import random

option = input("Enter a choice here: ")
options = []

while option != "":
    options.append(option)
    option = input("Enter a choice here: ")

print(random.choice(options))