"""Repeating a beat in a loop."""

__author__ = "730383357"

beat: str = input("What beat do you want to repeat? ")
i: int = 0
stop: int = int(input("How many times do you want to repeat it? "))
result: str = ""

if stop > 0:
    while i < stop - 1:
        result = result + beat + " "
        i = i + 1
    result = result + beat
    print(result)
else:
    print("No beat...")