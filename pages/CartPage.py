"""PageObject pattern for Cart page"""

from selenium.common.exceptions import NoSuchElementException
from pages.general_locators import GeneralSelectors
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from helpers.page_helpers import wait_for_element


class CartPage(BasePage):
    CART_BUTTON = (By.CSS_SELECTOR, '.col-sm-3 #cart')
    VIEW_CART = (By.XPATH, '//ul[@class="dropdown-menu pull-right"]//strong[text()=" View Cart"]')
    DROPDOWN_CHECKOUT = (By.XPATH, '//ul[@class="dropdown-menu pull-right"]//strong[text()=" Checkout"]')
    CONTINUE_SHOPPING = (By.XPATH, '//a[text()="Continue Shopping"]')
    CHECKOUT_BUTTON = (By.XPATH, '//a[text()="Checkout"]')
    UPDATE_BUTTON = (By.XPATH, '//button[@data-original-title="Update"]')
    REMOVE_BUTTON = (By.XPATH, '//button[@data-original-title="Remove"]')
    CONTINUE_BUTTON = (By.XPATH, '//a[text()="Continue"]')
    SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Success: You have modified your shopping cart!')]")

    def open_cart(self):
        self._click_to_element(self.CART_BUTTON)
        return self

    def click_view_cart(self):
        self._click_to_element(self.VIEW_CART)
        return self

    def click_checkout_cart(self):
        self._click_to_element(self.DROPDOWN_CHECKOUT)
        return self

    def click_update_product_in_cart(self):
        self._click_to_element(self.UPDATE_BUTTON)
        self._wait_for_visible(self.SUCCESS_TEXT)
        return self

    def click_remove_product_from_cart(self):
        self._click_to_element(self.REMOVE_BUTTON)
        self._wait_for_visible(self.CONTINUE_BUTTON)
        return self

    def continue_shopping(self):
        self._click_to_element(self.CONTINUE_SHOPPING)
