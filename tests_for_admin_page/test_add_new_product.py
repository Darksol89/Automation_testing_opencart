"""Test for adding new product via Admin page"""
import pytest
from helpers.page_helpers import wait_for_element
from helpers.database_helper import getDatabaseQuery
from PageObject.AdminDashPage import AdminDashboard


@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product(browser_driver, get_url, open_admin_dashboard, name, meta_tag, model):
    """Adding new product"""
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()

    # Check result
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()


@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product_and_check_database(browser_driver, get_url, open_admin_dashboard, name, meta_tag, model):
    """Adding new product"""
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)

    sql_query = 'SELECT * FROM oc_product WHERE model="Test_Model"'
    assert getDatabaseQuery(sql_query)


@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product_with_image(browser_driver, get_url, open_admin_dashboard, name, meta_tag, model):
    """Adding new product"""
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .upload_new_image() \
        .select_image_from_explorer() \
        .close_upload_window() \
        .save_element()

    # Check result
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()
