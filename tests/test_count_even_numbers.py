from problems.count_even_numbers import count_even_numbers


def test_basic() -> None:
    assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3


def test_all_even() -> None:
    assert count_even_numbers([2, 4, 6, 8]) == 4


def test_all_odd() -> None:
    assert count_even_numbers([1, 3, 5, 7]) == 0


def test_empty_list() -> None:
    assert count_even_numbers([]) == 0


def test_negative_numbers() -> None:
    assert count_even_numbers([-4, -3, -2, -1, 0]) == 3
