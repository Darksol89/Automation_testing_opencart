"""Selectors for different elements in the Opencart login page """
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PageObject.GeneralLocators import GeneralSelectors
from PageObject.BasePage import BasePage
from helpers.page_helpers import wait_for_element

# Create custom logger
logging.basicConfig(level=logging.INFO)
login_logger = logging.getLogger('Login Page')


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, 'input[type="submit"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    CONTINUE = (By.XPATH, "//div[@class='col-sm-6']//a[text()='Continue']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')

    def open_account_page(self):
        self._click_to_element(GeneralSelectors.OPEN_LOGIN_PAGE)
        login_logger.info('Open Login Page')
        return self

    def login_user(self, email, password):
        self._send_keys(email, self.EMAIL_INPUT)
        self._send_keys(password, self.PASSWORD_INPUT)
        self._click_to_element(self.LOGIN_SUBMIT)
        return self

    def register_new_user(self):
        try:
            wait_for_element(self.browser, self.CONTINUE)
            self._click_to_element(self.CONTINUE)
        except NoSuchElementException:
            print('Continue button is not available')

        return self

    def forgotten_password_form(self):
        try:
            wait_for_element(self.browser, self.FORGOTTEN_PASSWORD)
            self._click_to_element(self.FORGOTTEN_PASSWORD)
        except NoSuchElementException:
            print('Forgotten password button is not available')

        return self
