"""Test for different web element in Login page"""
import pytest
from pages.LoginPage import LoginPage


def test_login_admin(browser_driver, get_url):
    account_page = LoginPage(browser_driver)
    account_page.open_account_page()
    account_page.username_input()
    account_page.login_button()


@pytest.mark.parametrize('email', ['test@ro.ru'])
def test_email_input(browser_driver, get_url, email):
    account_page = LoginPage(browser_driver)
    account_page.open_account_page()
    account_page.email_input(email)


@pytest.mark.parametrize('password', ['1234'])
def test_password_input(browser_driver, get_url, password):
    account_page = LoginPage(browser_driver)
    account_page.open_account_page()
    account_page.password_input(password)


def test_open_new_customer_page(browser_driver, get_url):
    account_page = LoginPage(browser_driver)
    account_page.open_account_page()
    account_page.continue_button()


def test_open_forgotten_password_page(browser_driver, get_url):
    account_page = LoginPage(browser_driver)
    account_page.open_account_page()
    account_page.forgotten_password()
