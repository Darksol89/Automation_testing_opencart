"""Tests for visible other web element in the Opencart main page"""
from pages.main_page import Selectors

def test_logo_link(browser_driver, get_url):
    logo_link = browser_driver.find_element(*Selectors.main_logo_link)
    assert logo_link.is_displayed()

def test_swiper_header(browser_driver, get_url):
    assert browser_driver.find_element(*Selectors.swiper_head)

def test_swiper_footer(browser_driver, get_url):
    assert browser_driver.find_element(*Selectors.swiper_footer)

def test_feature_header(browser_driver, get_url):
    assert browser_driver.find_element(*Selectors.featured_header)