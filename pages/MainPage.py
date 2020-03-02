"""Selectors for different elements in the Opencart main page """
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.general_locators import GeneralSelectors
from pages.BasePage import BasePage
from helpers.page_helpers import wait_for_element


class MainPage(BasePage):
    PROMOBLOCK_HEAD = (By.CSS_SELECTOR, '.swiper-viewport #slideshow0')
    PROMOBLOCK_FOOTER = (By.CSS_SELECTOR, '.swiper-viewport #carousel0')
    PRODUCT_HEADER = (By.CSS_SELECTOR, 'h3')
    BUTTON_GROUP = (By.CSS_SELECTOR, '.button-group')
    PROMOBLOCK_NAV_BUTTON = (By.CSS_SELECTOR, '.swiper-pager .swiper-button-next')

    def promoblock_head(self):
        assert self.browser.find_element(*self.PROMOBLOCK_HEAD)

    def promoblock_footer(self):
        assert self.browser.find_element(*self.PROMOBLOCK_FOOTER)

    def product_header(self):
        assert self.browser.find_element(*self.PRODUCT_HEADER)

    def main_page_buttons(self):
        assert self.browser.find_elements(*self.BUTTON_GROUP)

    def promoblock_navigation_buttons(self):
        assert self.browser.find_elements(*self.PROMOBLOCK_NAV_BUTTON)