"""Test for different web element in Login page"""
import pytest
from PageObject import LoginPage


@pytest.mark.parametrize('email, password', [('test@ro.ru', '1234')])
def test_login_user(browser_driver, get_url, email, password):
    LoginPage(browser_driver) \
        .open_account_page() \
        .login_user(email, password)


def test_open_new_customer_page(browser_driver, get_url):
    LoginPage(browser_driver) \
        .open_account_page() \
        .register_new_user()

    assert browser_driver.title == 'Register Account'


def test_open_forgotten_password_page(browser_driver, get_url):
    LoginPage(browser_driver) \
        .open_account_page() \
        .forgotten_password_form()

    assert browser_driver.title == 'Forgot Your Password?'
