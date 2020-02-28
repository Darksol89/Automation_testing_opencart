"""Test for adding new product via Admin page"""
import pytest
from helpers.page_helpers import wait_for_element
from pages.admin_dashboard_page import AdminDashboard


@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product(browser_driver, get_url, open_admin_dashboard, name, meta_tag, model):
    # Open Product page from Catalog
    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG).click()
    browser_driver.find_element(*AdminDashboard.Navigation.CATALOG_PRODUCTS).click()
    # Add new product
    browser_driver.find_element(*AdminDashboard.Products.ADD_NEW).click()
    try:
        product_name = browser_driver.find_element(*AdminDashboard.ProductForm.PRODUCT_NAME)
        product_meta_tag = browser_driver.find_element(*AdminDashboard.ProductForm.META_TAG_TITLE)
        product_name.clear()
        product_name.send_keys(name)
        product_meta_tag.clear()
        product_meta_tag.send_keys(meta_tag)
        # Change tab
        browser_driver.find_element(*AdminDashboard.ProductForm.Tabs.DATA_TAB).click()
        # Input Model
        prod_model = browser_driver.find_element(*AdminDashboard.ProductForm.MODEL)
        prod_model.send_keys(model)
        browser_driver.find_element(*AdminDashboard.Products.SAVE_PRODUCT).click()
    except:
        print('Something wrong!')

    # Check result
    wait_for_element(browser_driver, AdminDashboard.Products.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.Products.SUCCESS_TEXT)

    assert success_text.is_displayed()
