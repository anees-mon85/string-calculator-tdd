from string_calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_number():
    assert add("1") == 1
