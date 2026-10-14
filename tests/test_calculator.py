from calculator import Calculator

def test_calculator_operations():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 2) == 3
    assert calc.multiply(4, 5) == 20
    assert calc.power(2, 3) == 8
