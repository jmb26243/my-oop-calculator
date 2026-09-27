import pytest

from calculator.calculation import Add, Subtract
from calculator.history import History


def test_history_starts_empty():
    history = History()

    assert history.get_all() == []

def test_history_stores_calculation():
	history = History()
	addition = Add(10,5)

	history.add(addition)

	assert history.get_all() == [addition]
def test_history_stores_multiple_calculations():
	history = History()
	addition = Add(10,5)
	subtraction = Subtract(20,7)

	history.add(addition)
	history.add(subtraction)

	assert history.get_all() == [addition, subtraction]
def test_get_all_does_not_expose_internal_list():
	history = History()
	addition = Add(10,5)

	history.add(addition)

	calculations = history.get_all()
	calculations.clear()

	assert history.get_all() == [addition]
def test_history_removes_calculation():
    history = History()
    addition = Add(10, 5)
    subtraction = Subtract(20, 7)

    history.add(addition)
    history.add(subtraction)

    removed = history.remove(0)

    assert removed == addition
    assert history.get_all() == [subtraction]
def test_history_remove_invalid_index():
    history = History()

    with pytest.raises(IndexError):
        history.remove(0)
def test_history_clears_all_calculations():
    history = History()
    addition = Add(10, 5)
    subtraction = Subtract(20, 7)

    history.add(addition)
    history.add(subtraction)

    history.clear()

    assert history.get_all() == []
