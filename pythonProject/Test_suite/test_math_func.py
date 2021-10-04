from Test_suite import math_func

def test_add():
    assert math_func.add(25, 75) == 100


def test_animal():
    assert 'dog' != 'wild'

def test_product():
    assert math_func.product(2, 19) == 38

def test_paychek():
    assert math_func.paycheck() == 52000