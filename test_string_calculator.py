from string_calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_number():
    assert add("1") == 1


def test_two_numbers_return_sum():
    assert add("1,2") == 3
