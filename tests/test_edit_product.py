from helpers.page_helpers import wait_for_element
from pages.admin_dashboard_page import AdminDashboard


def test_edit_product(browser_driver, get_url, open_admin_dashboard):
    """Test for Edit one of product"""
    # Open Product page from Catalog
    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG).click()
    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG_PRODUCTS).click()
    # Click Edit button
    wait_for_element(browser_driver, AdminDashboard.Products.EDIT)
    browser_driver.find_element(*AdminDashboard.Products.EDIT).click()
    # Modify product name
    wait_for_element(browser_driver, AdminDashboard.ProductForm.PRODUCT_NAME)
    product_name = browser_driver.find_element(*AdminDashboard.ProductForm.PRODUCT_NAME)
    product_name.clear()
    product_name.send_keys('TEST_PRODUCT')
    # Modify Meta Tag field
    wait_for_element(browser_driver, AdminDashboard.ProductForm.META_TAG_TITLE)
    meta_tag_title = browser_driver.find_element(*AdminDashboard.ProductForm.META_TAG_TITLE)
    meta_tag_title.clear()
    meta_tag_title.send_keys('TEST_META_TITLE')
    # Save results
    browser_driver.find_element(*AdminDashboard.Products.SAVE_PRODUCT).click()
    # Check result
    wait_for_element(browser_driver, AdminDashboard.Products.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.Products.SUCCESS_TEXT)

    assert success_text.is_displayed()
