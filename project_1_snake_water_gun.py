# snake, water, gun game

import random

comp = random.choice([-1, 0, 1])    # select random choice for comp from given values

user = input("Enter your choice (snake, gun, water): ")
userDict = {"snake": 1, "gun": 0, "water": -1}   # assign user choice for with numbers
userChoice =  userDict[user]

reverseDict = {1: "snake", 0: "gun", -1: "water"}   # assign como choice for with actual values

# by now we have two numbers: user and comp

print(f"Computer chose: {reverseDict[comp]}")
print(f"You chose: {reverseDict[userChoice]}")

if comp == userChoice:
    print("It's a draw")

else:    
    if comp == -1 and userChoice == 1:
        print("You win")
    elif comp == -1 and userChoice == 0:
        print("You lose")

    elif comp == 1 and userChoice == -1:
        print("You lose")
    elif comp == 1 and userChoice == 0:
        print("You win")

    elif comp == 0 and userChoice == -1:
        print("You win")
    elif comp == 0 and userChoice == 1:
        print("You lose")

    else:
        print("Something went wrong!")