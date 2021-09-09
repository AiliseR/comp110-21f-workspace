"""Example of conditional (if-else) statements."""
"""note to self: when variable name is all caps it's a constant"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else: 
        print("You guessed too low!")

"""note to self: indentation matters!"""

print("Game over.")