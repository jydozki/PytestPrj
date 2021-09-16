import pytest
import allure

@allure.description ("validate login")
@allure.severity (severity_level="CRITICAL")
@pytest.mark.smoke
def test_login():
    print("login done")

@allure.description("validate regression passed")
@allure.severity (severity_level="HIGH")
@pytest.mark.regression
def test_regression():
    print("regression done")

@allure.description ("validate logout")
@allure.severity (severity_level="NORMAL")
@pytest.mark.smoke
def test_logout():
    print("logout done")