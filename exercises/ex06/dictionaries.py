"""Practice with dictionaries."""

__author__ = "730383357"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Switch keys and values."""
    switched: dict[str, str] = {}
    for key in a:
        switched[key] = a[key]
    for key in a:
        switched[key] = key
    for key in a:
        key = a[key]
    return switched


def favorite_color(a: dict[str, str]) -> dict[str, str]:
    """Returns the color that appears most frequently."""