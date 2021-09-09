"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730383357"

from random import randint

fortune_one: str = ("You will be a light in the lives of others.")
fortune_two: str = ("Never doubt your self worth.")
fortune_three: str = ("People smile everywhere you go.")
fortune_four: str = ("The love you seek is within yourself.")

print("Your fortune cookie says...")

fortune_number: int = (randint(1, 4))

if fortune_number < 4:
    if fortune_number < 3:
        if fortune_number < 2:
            print(fortune_one)
        else: 
            print(fortune_two)
    else:
        print(fortune_three)
else:
    print(fortune_four)

print("Now, go spread positive vibes!")