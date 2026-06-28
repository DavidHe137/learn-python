from problems.largest_number import largest_number


def test_basic() -> None:
    assert largest_number([3, 7, 2, 9, 4]) == 9


def test_single_element() -> None:
    assert largest_number([42]) == 42


def test_negative_numbers() -> None:
    assert largest_number([-5, -1, -10]) == -1


def test_unsorted() -> None:
    assert largest_number([10, 2, 8, 10, 1]) == 10
