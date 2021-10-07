"""List utility functions."""

__author__ = "730383357"


def all(long: list[int], short: int) -> bool:
    """Return True if all values of long match short, False otherwise."""
    i: int = 0
    if len(long) > 0:
        while i < len(long):
            if long[i] != short:
                return False
            i += 1
        return True
    else:
        return False


def is_equal(a: list[int], b: list[int]) -> bool:
    """Returns True if a and b are deeply equal, False otherwise."""
    i: int = 0
    if len(a) == len(b):
        while i < len(a) and i < len(b):
            if a[i] != b[i]:
                return False
            i += 1
        return True
    else:
        return False


def max(large: list[int]) -> int:
    """Assess each item in the list, return the largest value."""
    if len(large) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        most: int = large[i]
        i += 1
        while i < len(large):
            if large[i] > most:
                most = large[i]
            i += 1
        return most