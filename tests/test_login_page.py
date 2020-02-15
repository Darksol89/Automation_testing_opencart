"""Test for different web element in Login page"""

from pages.login_page import LoginPage


def test_login_admin(browser_driver, get_url):
    browser_driver.find_element(*LoginPage.OPEN_LOGIN_PAGE).click()
    browser_driver.find_element(*LoginPage.CONTINUE)
    browser_driver.find_element(*LoginPage.EMAIL_INPUT)
    browser_driver.find_element(*LoginPage.FORGOTTEN_PASSWORD)
    browser_driver.find_element(*LoginPage.PASSWORD_INPUT)
    browser_driver.find_element(*LoginPage.SUBMIT)
