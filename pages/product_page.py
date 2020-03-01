"""Selectors for different elements in the Opencart product page """
from pages.general_locators import GeneralSelectors
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_CARD = (By.CSS_SELECTOR, '.form-group #button-cart')
    QUANTITY = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_WISH_LIST = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    COMPARE_PRODUCT = (By.XPATH, "//button[@data-original-title='Compare this Product']")
    RATING = (By.CSS_SELECTOR, '.rating')

    def open_product_page(self):
        self.click_to_element(GeneralSelectors.OPEN_MACBOOK_PRODUCT_PAGE)

    def add_to_card(self):
        assert self.browser.find_element(*self.ADD_TO_CARD)

    def quantity(self):
        assert self.browser.find_element(*self.QUANTITY)

    def add_to_wish_list(self):
        assert self.browser.find_element(*self.ADD_TO_WISH_LIST)

    def compare_product(self):
        assert self.browser.find_element(*self.COMPARE_PRODUCT)

    def rating(self):
        assert self.browser.find_element(*self.RATING)