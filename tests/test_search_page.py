"""Test for different web element in Search page"""

from pages.search_page import SearchPage
from pages.general_locators import GeneralSelectors


def test_search_page(browser_driver, get_url):
    browser_driver.find_element(*GeneralSelectors.OPEN_SEARCH_PAGE).click()
    browser_driver.find_element(*SearchPage.CATEGORIES_LIST)
    browser_driver.find_element(*SearchPage.CHECKBOX_DESCRIPTION)
    browser_driver.find_element(*SearchPage.CHECKBOX_SUBCATEGORIES)
    browser_driver.find_element(*SearchPage.INPUT_SEARCH)
    browser_driver.find_element(*SearchPage.SEARCH_BUTTON)
