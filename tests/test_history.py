import pytest

from calculator.calculation import Add, Calculation, Subtract
from calculator.history import History


def test_history_starts_empty():
    history = History()

    assert history.get_history() == []


def test_history_stores_calculations():
    history = History()
    addition = Add(10, 5)

    history.add(addition)

    assert history.get_history() == [addition]


def test_history_stores_multiple_calculations():
    history = History()
    addition = Add(10, 5)
    subtraction = Subtract(20, 7)

    history.add(addition)
    history.add(subtraction)

    assert history.get_history() == [addition, subtraction]


def test_get_history_does_not_expose_internal_list():
    history = History()
    addition = Add(10, 5)

    history.add(addition)

    calculations = history.get_history()
    calculations.clear()

    assert history.get_history() == [addition]


def test_history_removes_calculation():
    history = History()
    addition = Add(10, 5)
    subtraction = Subtract(20, 7)

    history.add(addition)
    history.add(subtraction)

    removed = history.remove(0)

    assert removed == addition
    assert history.get_history() == [subtraction]


def test_history_remove_invalid_index():
    history = History()

    with pytest.raises(IndexError):
        history.remove(0)


def test_history_rejects_non_calculation():
    history = History()

    with pytest.raises(TypeError):
        history.add("not a calculation")


def test_history_remove_negative_index():
    history = History()
    history.add(Add(10, 5))

    with pytest.raises(IndexError):
        history.remove(-1)


def test_history_remove_out_of_range_index():
    history = History()
    history.add(Add(10, 5))

    with pytest.raises(IndexError):
        history.remove(1)
def test_histories_are_independent():
    first = History()
    second = History()

    first.add(Add(10, 5))

    assert second.get_history() == []
