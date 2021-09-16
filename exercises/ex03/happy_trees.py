"""Drawing forests in a loop."""

__author__ = "730383357"

TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0

if depth > 0:
    while i < depth:
        print(TREE)
        TREE = TREE + '\U0001F332'
        i = i + 1