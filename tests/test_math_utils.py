from app.math_functions import add, subtract


def test_add():
    assert add(1, 4) == 5


def test_subtract():
    assert subtract(5, 2) == 3
