import pytest
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
def test_calculation_is_abstract():
    with pytest.raises(TypeError):
        Calculation(10, 5)


def test_polymorphism():
    calculations = [Add(10, 5), Subtract(20, 7)]

    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [15, 13]


def test_decimal_addition():
    assert Add(0.1, 0.2).get_result() == pytest.approx(0.3)


def test_decimal_subtraction():
    assert Subtract(1.5, 0.25).get_result() == 1.25
def test_abstract_calculation_method():
    class TestCalculation(Calculation):
        def get_result(self):
            return super().get_result()

    calculation = TestCalculation(10, 5)
    assert calculation.get_result() is None
