"""Test for different web element in Search page"""

from PageObject.SearchPage import SearchPage


def test_input_for_search(browser_driver, get_url):
    search_page = SearchPage(browser_driver)
    search_page.open_search_page()
    search_page.search_result(word='Test')

    assert browser_driver.title == 'Search - Test'


def test_subcategories_checkbox_disabled(browser_driver, get_url):
    search_page = SearchPage(browser_driver)
    search_page.open_search_page()
    search_page.checkbox_subcategories_disabled()


def test_subcategories_checkbox_enable(browser_driver, get_url):
    search_page = SearchPage(browser_driver)
    search_page.open_search_page()
    search_page.select_categories(option='Desktops')
    search_page.checkbox_subcategories_enable()


def test_select_categories(browser_driver, get_url):
    search_page = SearchPage(browser_driver)
    search_page.open_search_page()
    search_page.select_categories(option='Desktops')


def test_product_description_checkbox(browser_driver, get_url):
    search_page = SearchPage(browser_driver)
    search_page.open_search_page()
    search_page.checkbox_description()
