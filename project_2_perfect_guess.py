# perfect guess game

import random

comp_guess = random.randint(1, 9)

# a = -1
guesses = 0
while True: #a != comp_guess:
    user_input = input("Enter your guess (0, 9): ")
    try:
        guesses += 1
        user_guess = int(user_input)
        if user_guess > comp_guess:
            print("Entered guess is higher, lower number please!")
        elif user_guess < comp_guess:
            print("Entered guess is lower, higher number please!")
        elif user_guess == comp_guess:
            print(f"You have correctly guessed the number: {comp_guess}")
            break
            # a = comp_guess
            
    except ValueError:
        print("WTF did you enter? ")
        print("Come on you have EYES, READ PROPERLY!")

print(f"Number of guesses you took: {guesses}")