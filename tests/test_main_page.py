"""Tests for visible other web element in the Opencart main page"""
from pages.main_page import MainPage


def test_main_page(browser_driver, get_url):
    browser_driver.find_element(*MainPage.PROMOBLOCK_HEAD)
    browser_driver.find_element(*MainPage.PROMOBLOCK_FOOTER)
    browser_driver.find_element(*MainPage.PRODUCT_HEADER)
    browser_driver.find_elements(*MainPage.BUTTON_GROUP)
    browser_driver.find_elements(*MainPage.PROMOBLOCK_NAV_BUTTON)
