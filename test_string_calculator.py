import pytest
from string_calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_number():
    assert add("1") == 1


def test_two_numbers_return_sum():
    assert add("1,2") == 3


def test_multiple_numbers_return_sum():
    assert add("1,2,3") == 6


def test_newlines_between_numbers():
    assert add("1\n2,3") == 6


def test_custom_delimiter():
    assert add("//;\n1;2") == 3


def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
        add("-1,2")


def test_multiple_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1,-2"):
        add("-1,-2,3")