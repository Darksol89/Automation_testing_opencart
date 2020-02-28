"""Selectors for different elements in the Opencart login page """
from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    SUBMIT = (By.CSS_SELECTOR, 'input[type="submit"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    CONTINUE = (By.XPATH, "//div[@class='col-sm-6']//a[text()='Continue']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')

