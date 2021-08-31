"""Types within variables and numeric operations."""

__author__ = "730383357"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")

exponentiation_result: str = str(int(left_hand_side) ** int(right_hand_side))
division_result: str = str(int(left_hand_side) / int(right_hand_side))
int_division_result: str = str(int(left_hand_side) // int(right_hand_side))
division_remainder: str = str(int(left_hand_side) % int(right_hand_side))
"""I know that line 12 is technically called a modulus?? But I don't want to risk mispelling it and I don't want to google it because that's using outside resources. Sorry :/."""

print(left_hand_side + " ** " + right_hand_side + " is " + exponentiation_result)
print(left_hand_side + " / " + right_hand_side + " is " + division_result)
print(left_hand_side + " // " + right_hand_side + " is " + int_division_result)
print(left_hand_side + " % " + right_hand_side + " is " + division_remainder)

"""Man I love this stuff I wish I could major in this without taking so much calculus."""