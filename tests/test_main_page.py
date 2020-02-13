"""Tests for visible other web element in the Opencart main page"""
from pages.main_page import MainPage


# def test_swiper_header(browser_driver, get_url):
#     assert browser_driver.find_element(*MainPage.PROMOBLOCK_HEAD)
#
#
# def test_swiper_footer(browser_driver, get_url):
#     assert browser_driver.find_element(*MainPage.PROMOBLOCK_FOOTER)
#
#
# def test_feature_header(browser_driver, get_url):
#     assert browser_driver.find_element(*MainPage.PRODUCT_HEADER)
#
#
# def test_button_group(browser_driver, get_url):
#     btn_group = browser_driver.find_elements(*MainPage.BUTTON_GROUP)
#     assert len(btn_group) == 4
#
#
# def test_swiper_button(browser_driver, get_url):
#     swiper_btn = browser_driver.find_elements(*MainPage.PROMOBLOCK_NAV_BUTTON)
#     assert len(swiper_btn) == 2

def test_main_page(browser_driver, get_url):
    browser_driver.find_element(*MainPage.PROMOBLOCK_HEAD)
    browser_driver.find_element(*MainPage.PROMOBLOCK_FOOTER)
    browser_driver.find_element(*MainPage.PRODUCT_HEADER)
    browser_driver.find_elements(*MainPage.BUTTON_GROUP)
    browser_driver.find_elements(*MainPage.PROMOBLOCK_NAV_BUTTON)
