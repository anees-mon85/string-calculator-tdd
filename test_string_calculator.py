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


def test_ignore_numbers_greater_than_1000():
    assert add("2,1001") == 2
    assert add("1000,2") == 1002


def test_delimiters_of_any_length():
    assert add("//[***]\n1***2***3") == 6


def test_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6


def test_multiple_delimiters_with_length_longer_than_one():
    assert add("//[***][%%%]\n1***2%%%3") == 6
