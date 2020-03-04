"""Selectors for different elements in the Opencart main page """
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class MainPage(BasePage):
    PROMOBLOCK_HEAD = (By.CSS_SELECTOR, '.swiper-viewport #slideshow0')
    PROMOBLOCK_FOOTER = (By.CSS_SELECTOR, '.swiper-viewport #carousel0')
    PRODUCT_HEADER = (By.XPATH, '//h3[text()="Featured"]')
    ADD_TO_CARD_BUTTON = (By.XPATH, '//span[text()="Add to Cart"]')


    def promoblock_head(self):
        self._wait_for_visible(self.PROMOBLOCK_HEAD)
        return self

    def promoblock_footer(self):
        self._wait_for_visible(self.PROMOBLOCK_FOOTER)
        return self

    def get_product_header(self):
        self._wait_for_visible(self.PRODUCT_HEADER)
        return self

    def add_to_card_button(self):
        self.browser.find_element(*self.ADD_TO_CARD_BUTTON).is_enabled()
        return self

