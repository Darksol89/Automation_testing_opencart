"""Test for different web element in Catalog page"""
import pytest
from pages.CatalogPage import CatalogPage
from pages.general_locators import GeneralSelectors


def test_catalog_page(browser_driver, get_url):
    browser_driver.find_element(*GeneralSelectors.OPEN_TABLETS_CATALOG_PAGE).click()
    browser_driver.find_element(*CatalogPage.GRID_BUTTON)
    browser_driver.find_element(*CatalogPage.LIST_BUTTON)
    browser_driver.find_element(*CatalogPage.PRODUCT_TREE)
    browser_driver.find_element(*CatalogPage.SHOW_COMBOBOX)
    browser_driver.find_element(*CatalogPage.SORT_BY_COMBOBOX)


def test_list_view_button(browser_driver, get_url):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .list_button_active()


def test_grid_view_button(browser_driver, get_url):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .grid_button_active()


@pytest.mark.parametrize('sort_option', ['Rating (Lowest)'])
def test_checking_sort_by(browser_driver, get_url, sort_option):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .select_from_sort_by(sort_option)

    check_result = browser_driver.find_element(*CatalogPage.SORT_BY_SELECTED).text

    assert str(check_result) == str(sort_option)


@pytest.mark.parametrize('show_option', ['100'])
def test_checking_show_value(browser_driver, get_url, show_option):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .select_show_element(show_option)

    check_result = browser_driver.find_element(*CatalogPage.SHOW_VALUE_SELECTED).text

    assert str(check_result) == str(show_option)
