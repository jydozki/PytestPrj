import pytest
@pytest.mark.smoke
def test_login():
    print("login done")

@pytest.mark.regression
def test_regression():
    print("regression done")

@pytest.mark.smoke
def test_logout():
    print("logout done")