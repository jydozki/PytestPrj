import allure
from Test_suite import math_func


def test_add():
    assert math_func.add(7, 3) == 10


def test_product():
    assert math_func.product(8, 12) == 96

def test_paychek():
    assert math_func.paycheck() == 52000