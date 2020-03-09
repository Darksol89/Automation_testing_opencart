"""Different tests for web elements in Cart page"""
import pytest
from PageObject import ProductPage, CartPage


def test_update_product(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart() \
        .click_update_product_in_cart()


def test_remove_product(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart() \
        .click_remove_product_from_cart()


def test_continue_shopping(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart() \
        .continue_shopping()

    assert browser_driver.browser.title == 'Your Store'
