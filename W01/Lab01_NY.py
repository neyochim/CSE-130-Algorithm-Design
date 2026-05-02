# 1. Name:
#    Nathan Yochim
# 2. Assignment Name:
#    Lab 01: Guessing Game
# 3. Assignment Description:
#    This program asks the user for a positive integer, picks a random number
#    between 1 and that integer, and then keeps track of each guess until the
#    correct number is found.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was making sure the loop and the guess list worked
#    together correctly. I had to think carefully about when to store each
#    guess and when to stop the loop so the final guess would still be counted.
# 5. How long did it take for you to complete the assignment?
#    1.5 hours

import random

# Game introduction.
print("This is the \"guess a number\" game.")
print("You try to guess a random number in the smallest number of attempts.")
print()

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Pick a positive integer: "))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {value_max}.")

# Initialize the sentinal and the array of guesses.

guesses = []

# Play the guessing game.

# Prompt the user for a number.
guess = int(input("> "))

while guess != value_random:
    guesses.append(guess)

    # Make a decision: was the guess too high, too low, or just right.
    if guess > value_random:
        print("\tToo high!")
    else:
        print("\tToo low!")

    guess = int(input("> "))

# Store the number in an array so it can be displayed later.
guesses.append(guess)

# Give the user a report: How many guesses and what the guesses where.
print(f"You were able to find the number in {len(guesses)} guesses.")
print(f"The numbers you guessed were: {guesses}")
