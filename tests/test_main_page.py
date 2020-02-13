"""Tests for visible other web element in the Opencart main page"""
from pages.main_page import Selectors


def test_swiper_header(browser_driver, get_url):
    assert browser_driver.find_element(*Selectors.swiper_head)


def test_swiper_footer(browser_driver, get_url):
    assert browser_driver.find_element(*Selectors.swiper_footer)


def test_feature_header(browser_driver, get_url):
    assert browser_driver.find_element(*Selectors.featured_header)


def test_button_group(browser_driver, get_url):
    btn_group = browser_driver.find_elements(*Selectors.button_group)
    assert len(btn_group) == 4


def test_swiper_button(browser_driver, get_url):
    swiper_btn = browser_driver.find_elements(*Selectors.swiper_buttons)
    assert len(swiper_btn) == 2
