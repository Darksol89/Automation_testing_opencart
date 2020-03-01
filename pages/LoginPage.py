"""Selectors for different elements in the Opencart login page """
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.general_locators import GeneralSelectors
from pages.BasePage import BasePage
from helpers.page_helpers import wait_for_element


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    SUBMIT = (By.CSS_SELECTOR, 'input[type="submit"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    CONTINUE = (By.XPATH, "//div[@class='col-sm-6']//a[text()='Continue']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')

    def open_account_page(self):
        self.click_to_element(GeneralSelectors.OPEN_LOGIN_PAGE)

    def email_input(self, email):
        try:
            wait_for_element(self.browser, self.EMAIL_INPUT)
            self.send_keys(email, self.EMAIL_INPUT)
        except NoSuchElementException:
            print('Email field is not available')

        assert self.browser.find_element(*self.EMAIL_INPUT).get_attribute('value') == email

    def username_input(self):
        assert self.browser.find_element(*self.USERNAME_INPUT)

    def password_input(self, password):
        try:
            wait_for_element(self.browser, self.PASSWORD_INPUT)
            self.send_keys(password, self.PASSWORD_INPUT)
        except NoSuchElementException:
            print('Password field is not available')

        assert self.browser.find_element(*self.PASSWORD_INPUT).is_displayed()

    def continue_button(self):
        try:
            wait_for_element(self.browser, self.CONTINUE)
            self.click_to_element(self.CONTINUE)
        except NoSuchElementException:
            print('Continue button is not available')

        assert self.browser.title == 'Register Account'

    def forgotten_password(self):
        try:
            wait_for_element(self.browser, self.FORGOTTEN_PASSWORD)
            self.click_to_element(self.FORGOTTEN_PASSWORD)
        except NoSuchElementException:
            print('Forgotten password button is not available')

        assert self.browser.title == 'Forgot Your Password?'

    def login_button(self):
        assert self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()
