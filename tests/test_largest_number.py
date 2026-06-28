from problems.largest_number import largest_number


def test_basic():
    assert largest_number([3, 7, 2, 9, 4]) == 9


def test_single_element():
    assert largest_number([42]) == 42


def test_negative_numbers():
    assert largest_number([-5, -1, -10]) == -1


def test_unsorted():
    assert largest_number([10, 2, 8, 10, 1]) == 10
