from calculator.calculation import Add, Subtract, Calculation


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

def test_subtract_two_positive_numbers():
    subtraction = Subtract(20, 7)
    result = subtraction.get_result()
    assert result == 13


def test_subtract_negative_and_positive():
    subtraction = Subtract(-10, 5)
    result = subtraction.get_result()
    assert result == -15
def test_add_is_a_calculation():
    addition = Add(10, 5)
    assert isinstance(addition, Calculation)


def test_subtract_is_a_calculation():
    subtraction = Subtract(10, 5)
    assert isinstance(subtraction, Calculation)
