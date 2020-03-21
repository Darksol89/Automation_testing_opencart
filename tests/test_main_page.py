"""Tests for visible other web element in the Opencart main page"""
from PageObject.MainPage import MainPage


def test_main_page(browser_driver, get_url):
    MainPage(browser_driver) \
        .logger_message() \
        .promoblock_head() \
        .promoblock_footer() \
        .add_to_card_button() \
        .get_product_header()


def test_promoblocks(browser_driver, get_url):
    MainPage(browser_driver) \
        .logger_message() \
        .promoblock_head() \
        .promoblock_footer()


def test_verify_feature_header(browser_driver, get_url):
    MainPage(browser_driver) \
        .logger_message() \
        .get_product_header()


def test_add_to_card_button(browser_driver, get_url):
    MainPage(browser_driver) \
        .logger_message() \
        .add_to_card_button() \
        ._click_to_element(MainPage.ADD_TO_CARD_BUTTON)
