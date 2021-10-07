"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730383357"


def test_only_evens_edge() -> None:
    """What happens if there's nothing in the list?"""
    even: list[int] = []
    assert only_evens(even) == []


def test_only_evens_first_use() -> None:
    """What happens if there's multiple of the same number in the list?"""
    even: list[int] = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    assert only_evens(even) == [2, 4, 4, 2]


def test_only_evens_second_use() -> None:
    """What happens if there's only one even number in the list?"""
    even: list[int] = [1, 9, 3, 9, 0, 5]
    assert only_evens(even) == [0]


def test_sub_edge() -> None:
    """What happens if the start is greater than len(a_list)?"""
    a_list: list[int] = [11, 5, 7, 2]
    start: int = 7
    end: int = 9
    assert sub(a_list, start, end) == []


def test_sub_first_use() -> None:
    """What happens if the indexes are between the the beginning and end of the list?"""
    a_list: list[int] = [4, 18, 3, 9, 15]
    start: int = 2
    end: int = 4
    assert sub(a_list, start, end) == [3, 9]


def test_sub_second_use() -> None:
    """What happens if the indexes are at the ends of the list?"""
    a_list: list[int] = [9, 4, 3, 2]
    start: int = 0
    end: int = 4
    assert sub(a_list, start, end) == [9, 4, 3, 2]


def test_concat_edge() -> None:
    """What happens if the first list is empty?"""
    first_list: list[int] = []
    second_list: list[int] = [5, 6, 43, 2]
    assert concat(first_list, second_list) == [5, 6, 43, 2]


def test_concat_first_use() -> None:
    """What happens if the second list is repetitive?"""
    first_list: list[int] = [3, 2, 4, 5]
    second_list: list[int] = [8, 8, 8]
    assert concat(first_list, second_list) == [3, 2, 4, 5, 8, 8, 8]


def test_concat_second_use() -> None:
    """What happens if there's multiple of the same number in the lists?"""
    first_list: list[int] = [3, 3, 4]
    second_list: list[int] = [4, 3, 3]
    assert concat(first_list, second_list) == [3, 3, 4, 4, 3, 3]