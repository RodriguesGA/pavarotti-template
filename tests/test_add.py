"""Tests for the add and add_wrong functions."""

from my_project.utils import add, add_wrong


def test_add_positive() -> None:
    assert add(1, 1) == 2


def test_add_negative() -> None:
    assert add(-1, -1) == -2


def test_add_zero() -> None:
    assert add(0, 5) == 5


def test_add_wrong_positive() -> None:
    assert add_wrong(1, 1) == 2


def test_add_wrong_negative() -> None:
    assert add_wrong(-1, -1) == -2


def test_add_wrong_zero() -> None:
    assert add_wrong(0, 5) == 5


def test_add_and_add_wrong_same_behavior() -> None:
    assert add(1, 1) == add_wrong(1, 1)
    assert add(-3, 5) == add_wrong(-3, 5)
