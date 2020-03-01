"""Test different web elements in Product page"""
import pytest
from pages.ProductPage import ProductPage


def test_product_page(browser_driver, get_url):
    product_page = ProductPage(browser_driver)
    product_page.open_product_page()
    product_page.compare_product()
    product_page.add_to_wish_list()


@pytest.mark.parametrize('qty', ['10'], ids=['quantity=10'])
def test_product_quantity(browser_driver, get_url, qty):
    """Test for input in quantity field"""
    product_page = ProductPage(browser_driver)
    product_page.open_product_page()
    product_page.quantity(qty)


def test_add_to_card_button(browser_driver, get_url):
    """Test for Add to Card button"""
    product_page = ProductPage(browser_driver)
    product_page.open_product_page()
    product_page.add_to_card()


def test_rating_stage(browser_driver, get_url):
    """Test for rating stage"""
    product_page = ProductPage(browser_driver)
    product_page.open_product_page()
    product_page.rating()
