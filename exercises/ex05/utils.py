"""List utility functions part 2."""

__author__ = "730383357"


def only_evens(even: list[int]) -> list[int]:
    """Return a list containing only the ints that are even."""
    i: int = 0
    even_list: list[int] = []
    while i < len(even):
        if even[i] % 2 == 0:
            even_list.append(even[i])
        i += 1
    return even_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Generate a list that's a subset of a_list and between the two indexes."""
    sub_list: list[int] = []
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return []
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    while start < end:
        sub_list.append(a_list[start])
        start += 1
    return sub_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Create a new list, adding the ints from second_list after the ints of first_list."""
    final_list: list[int] = []
    i: int = 0
    while i < len(first_list):
        final_list.append(first_list[i])
        i += 1
    i = 0
    while i < len(second_list):
        final_list.append(second_list[i])
        i += 1
    return final_list