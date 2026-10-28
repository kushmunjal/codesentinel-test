"""Unit tests for the enhanced Calculator class."""

import pytest
from calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0


def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5


def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 100) == 0


def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(7, 2) == 3.5

    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -1) == 0.5

    with pytest.raises(ValueError):
        calc.power(0, -2)
