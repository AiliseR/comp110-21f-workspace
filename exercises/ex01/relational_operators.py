"""Practicing more operators and switching between classes of info."""
"""AKA repeating what we just did but this time with Booleans :)""" """I'm having way too much fun with docstrings please don't take off points for this."""

__author__ = "730383357"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")

less_than_result: str = str(int(left_hand_side) < int(right_hand_side))
greater_than_or_equal: str = str(int(left_hand_side) >= int(right_hand_side))
equal_to_result: str = str(int(left_hand_side) == int(right_hand_side))
not_equal_to: str = str(int(left_hand_side) != int(right_hand_side))
"""This is a copy of my other code and I hope you see that as clever instead of lazy."""

print(left_hand_side + " < " + right_hand_side + " is " + less_than_result)
print(left_hand_side + " >= " + right_hand_side + " is " + greater_than_or_equal)
print(left_hand_side + " == " + right_hand_side + " is " + equal_to_result)
print(left_hand_side + " != " + right_hand_side + " is " + not_equal_to)

"""My apologies for the long variable names. I'm a lot of things but concise is not one of them."""