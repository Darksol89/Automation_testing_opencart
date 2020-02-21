from pages.admin_dashboard_page import AdminDashboard
from selenium.webdriver.common.alert import Alert
from helpers import page_helpers


def test_delete_product(browser_driver, get_url, open_admin_dashboard):
    """Test for delete one of product"""

    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG).click()
    page_helpers.wait_for_element(browser_driver, AdminDashboard.Navigation.CATALOG_PRODUCTS)
    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG_PRODUCTS).click()
    # Check product from table
    page_helpers.wait_for_element(browser_driver, AdminDashboard.Products.PRODUCT_51)
    product_checkbox = browser_driver.find_element(*AdminDashboard.Products.PRODUCT_51)
    product_checkbox.click()
    # Delete product
    browser_driver.find_element(*AdminDashboard.Products.REMOVE).click()
    Alert(browser_driver).accept()
    assert product_checkbox.size == 0

