"""Test different web elements in Product page"""
import pytest
from pages import ProductPage, CartPage


@pytest.mark.parametrize('qty', ['10'], ids=['quantity=10'])
def test_product_quantity(browser_driver, get_url, qty):
    """Test for input in quantity field"""
    ProductPage(browser_driver) \
        .open_product_page() \
        .quantity(qty)


def test_add_to_card_button(browser_driver, get_url):
    """Test for Add to Card button"""
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()


def test_rating_stage(browser_driver, get_url):
    """Test for rating stage"""
    ProductPage(browser_driver).open_product_page() \
        .rating()


def test_add_product_to_cart(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart()

    assert browser_driver.title == 'Shopping Cart'


def test_product_checkout(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_checkout_cart()
