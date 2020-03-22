"""Different tests for web elements in Cart page"""
import allure
from PageObject import ProductPage, CartPage

@allure.title('Test for update product')
def test_update_product(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart() \
        .click_update_product_in_cart()

@allure.title('Test for remove product')
def test_remove_product(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart() \
        .click_remove_product_from_cart()

@allure.title('Test for continue shopping button')
def test_continue_shopping(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart() \
        .continue_shopping()

    assert browser_driver.browser.title == 'Your Store'
