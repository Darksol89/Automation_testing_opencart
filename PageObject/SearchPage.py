"""Selectors for different elements in the Opencart search page """
import logging
from selenium.webdriver.common.by import By
from PageObject.GeneralLocators import GeneralSelectors
from PageObject.BasePage import BasePage

# Create custom logger
logger = logging.getLogger('Search Page')


class SearchPage(BasePage):
    INPUT_SEARCH = (By.CSS_SELECTOR, '#input-search')
    CATEGORIES_LIST = (By.XPATH, "//select[@name='category_id']")
    CHECKBOX_DESCRIPTION = (By.CSS_SELECTOR, '#description')
    CHECKBOX_SUBCATEGORIES = (By.XPATH, "//input[@name='sub_category']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="button"]')

    def open_search_page(self):
        self._click_to_element(GeneralSelectors.OPEN_SEARCH_PAGE)
        logger.info('Open Search Page')

    def select_categories(self, option):
        self._selecting_by_visible_text(self.CATEGORIES_LIST, text=option)
        return self

    def checkbox_description(self):
        self._click_to_element(self.CHECKBOX_DESCRIPTION)
        return self

    def checkbox_subcategories_disabled(self):
        self.driver.find_element(*self.CHECKBOX_SUBCATEGORIES).get_attribute('disabled')
        return self

    def checkbox_subcategories_enable(self):
        self._click_to_element(self.CHECKBOX_SUBCATEGORIES)
        return self

    def search_result(self, word):
        self._send_keys(word, self.INPUT_SEARCH)
        self._click_to_element(self.SEARCH_BUTTON)
        return self
