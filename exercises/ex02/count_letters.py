"""Counting letters in a string."""

__author__ = "730383357"

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
length: int = len(word)
i: int = 0
count: int = 0

while i < length:
    if (word[i]) == letter:
        count = count + 1
    i = i + 1

print("Count: " + str(count))