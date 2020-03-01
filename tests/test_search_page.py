"""Test for different web element in Search page"""

from pages.search_page import SearchPage


def test_search_page(browser_driver, get_url):
    search_page = SearchPage(browser_driver)
    search_page.open_search_page()
    search_page.input_search()
    search_page.categories_list()
    search_page.checkbox_description()
    search_page.checkbox_subcategories()
    search_page.search_button()
