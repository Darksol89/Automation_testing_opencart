from pages.admin_dashboard_page import AdminDashboard
from selenium.webdriver.common.alert import Alert
from helpers.page_helpers import wait_for_element


def test_delete_product(browser_driver, get_url, open_admin_dashboard):
    """Test for delete test product"""

    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG).click()
    wait_for_element(browser_driver, AdminDashboard.Navigation.CATALOG_PRODUCTS)
    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG_PRODUCTS).click()
    # Find test product
    wait_for_element(browser_driver, AdminDashboard.Products.TEST_PRODUCT_FOR_REMOVE)
    product_checkbox = browser_driver.find_element(*AdminDashboard.Products.TEST_PRODUCT_FOR_REMOVE)
    product_checkbox.click()
    # Copy product
    browser_driver.find_element(*AdminDashboard.Products.COPY).click()
    # Delete product
    wait_for_element(browser_driver, AdminDashboard.Products.TEST_PRODUCT_FOR_REMOVE)
    product_checkbox = browser_driver.find_element(*AdminDashboard.Products.TEST_PRODUCT_FOR_REMOVE)
    product_checkbox.click()
    browser_driver.find_element(*AdminDashboard.Products.REMOVE).click()
    Alert(browser_driver).accept()
    # Check result
    wait_for_element(browser_driver, AdminDashboard.Products.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.Products.SUCCESS_TEXT)

    assert success_text.is_displayed()
