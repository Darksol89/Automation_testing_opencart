"""Tests for visible other web element in the Opencart main page"""
from pages.main_page import MainPage


def test_main_page(browser_driver, get_url):
    main_page = MainPage(browser_driver)
    main_page.promoblock_head()
    main_page.promoblock_footer()
    main_page.promoblock_navigation_buttons()
    main_page.main_page_buttons()
    main_page.product_header()
    
