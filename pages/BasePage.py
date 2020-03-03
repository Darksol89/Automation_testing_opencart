"""Base Page in Page Object pattern"""
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser):
        """Initialize web driver"""
        self.browser: WebDriver = browser

    def _click_to_element(self, locator):
        """Click to web element"""
        try:
            self.browser.implicitly_wait(3)
            WebDriverWait(self.browser, 5).until(ec.presence_of_element_located(locator))
        except NoSuchElementException:
            print('Element is not found')
        finally:
            self.browser.find_element(*locator).click()

    def _send_keys(self, value, locator):
        """Send keys to specified locator"""
        element = self.browser.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def _selecting_by_visible_text(self, locator, text):
        """Selecting visible options from combo box"""
        select = Select(self.browser.find_element(*locator))
        select.select_by_visible_text(text)

    def _get_element_text(self, locator):
        """Get text from web element"""
        return self.browser.find_element(locator).text

    def _wait_for_visible(self, locator, time_wait=3):
        return WebDriverWait(self.browser, time_wait).until(ec.visibility_of(self.browser.find_element(*locator)))
