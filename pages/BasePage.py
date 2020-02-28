"""Base Page in Page Object pattern"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class BasePage:

    def __init__(self, browser):
        """Initialize web driver"""
        self.browser: WebDriver = browser


    def click_to_element(self, locator):
        """Click to web element"""
        try:
            WebDriverWait(self.browser, 5).until(ec.presence_of_element_located(locator))
        except NoSuchElementException:
            print('Element is not found')
        finally:
            self.browser.find_element(*locator).click()

    def send_keys(self, value, locator):
        """Send keys to specified locator"""
        element = self.browser.find_element(*locator)
        element.clear()
        element.send_keys(value)