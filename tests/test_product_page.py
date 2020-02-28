"""Test different web elements in Product page"""
import pytest
from pages.product_page import ProductPage
from helpers.page_helpers import wait_for_element
from selenium.common.exceptions import NoSuchElementException
from pages.general_locators import GeneralSelectors

def test_product_page(browser_driver, get_url):
    browser_driver.find_element(*GeneralSelectors.OPEN_MACBOOK_PRODUCT_PAGE).click()
    browser_driver.find_element(*ProductPage.ADD_TO_CARD)
    browser_driver.find_element(*ProductPage.ADD_TO_WISH_LIST)
    browser_driver.find_element(*ProductPage.COMPARE_PRODUCT)
    browser_driver.find_element(*ProductPage.QUANTITY)
    browser_driver.find_element(*ProductPage.RATING)


@pytest.mark.parametrize('qty', ['10'], ids=['quantity=10'])
def test_product_quantity(browser_driver, get_url, qty):
    """Test for input in quantity field"""
    browser_driver.find_element(*ProductPage.OPEN_PRODUCT_PAGE).click()
    wait_for_element(browser_driver, ProductPage.QUANTITY)
    try:
        quantity_field = browser_driver.find_element(*ProductPage.QUANTITY)
        quantity_field.clear()
        quantity_field.send_keys(qty)
    except NoSuchElementException:
        print('Quantity field is not available')

    assert quantity_field.get_attribute('value') == qty


def test_add_to_card_button(browser_driver, get_url):
    """Test for Add to Card button"""
    browser_driver.find_element(*ProductPage.OPEN_PRODUCT_PAGE).click()
    wait_for_element(browser_driver, ProductPage.ADD_TO_CARD)
    try:
        add_to_card_button = browser_driver.find_element(*ProductPage.ADD_TO_CARD)
        add_to_card_button.click()
    except NoSuchElementException:
        print('Add to Card button is not displayed')

    assert add_to_card_button.is_displayed()


def test_rating_stage(browser_driver, get_url):
    """Test for rating stage"""
    browser_driver.find_element(*ProductPage.OPEN_PRODUCT_PAGE).click()
    wait_for_element(browser_driver, ProductPage.RATING)
    try:
        rating = browser_driver.find_element(*ProductPage.RATING)
        rating.is_displayed()
    except NoSuchElementException:
        print('Rating stage is not displayed')

    assert rating.is_displayed()
