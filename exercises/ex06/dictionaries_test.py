"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color

__author__ = "730383357"


def test_invert_edge() -> None:
    assert invert({'a': 'apple', 'b': 'apple', 'c': 'cheese'}) == KeyError


def test_invert_use1() -> None:
    assert invert({'a': 'apple', 'b': 'bread', 'c': 'cheese'}) == {'apple': 'a', 'bread': 'b', 'cheese': 'c'}


def test_invert_use2() -> None:
    assert invert({'d': 'danish', 'e': 'eggs', 'f': 'fondue'}) == {'danish': 'd', 'eggs': 'e', 'fondue': 'f'}


def test_favorite_color_edge() -> None:
    assert favorite_color({'Ryan': 'blue'}) == 'blue'


def test_favorite_color_use1() -> None:
    assert favorite_color({'Ryan': 'blue', 'Caro': 'yellow', 'Mercy': 'blue', 'Sarah': 'pink'}) == 'blue'


def test_favorite_color_use2() -> None:
    assert favorite_color({'Ryan': 'blue', 'Caro': 'pink', 'Mercy': 'blue', 'Sarah': 'pink'}) == 'blue'