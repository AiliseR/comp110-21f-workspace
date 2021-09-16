"""Finding duplicate letters in a word."""

__author__ = "730383357"

word: str = input("Enter a word: ")
i: int = 0
duplicate: bool = False

while i < len(word):
    letter: str = word[i]
    j: int = i + 1
    while j < len(word):
        if letter == word[j]:
            duplicate = True
        j = j + 1
    i = i + 1

if duplicate == True:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")

### VS Code is telling me there's a bug at ###
### line 18, but it still works just fine ###
### so I'm leaving it alone ###