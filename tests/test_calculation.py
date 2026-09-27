from calculator.calculation import Add


def test_add_two_positive_numbers():
    addition = Add(10, 5)
    result = addition.get_result()
    assert result == 15


def test_add_negative_and_positive():
    addition = Add(-10, 5)
    result = addition.get_result()
    assert result == -5


def test_add_zero():
    addition = Add(10, 0)
    result = addition.get_result()
    assert result == 10


def test_add_two_negative_numbers():
    addition = Add(-10, -5)
    result = addition.get_result()
    assert result == -15

