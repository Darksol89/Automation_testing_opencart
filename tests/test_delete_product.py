import pytest
from PageObject.AdminDashPage import AdminDashboard
from selenium.webdriver.common.alert import Alert
from helpers.page_helpers import wait_for_element
from helpers.database_helper import getDatabaseQuery


@pytest.mark.parametrize('name, meta_tag, model', [('Test_123', '123_Tag', '123_model')])
def test_delete_product(browser_driver, get_url, open_admin_dashboard, name, meta_tag, model):
    """Test for delete test product"""
    # Adding new product
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)
    # Delete product
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .remove_element()
    Alert(browser_driver).accept()
    # Check result
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()


@pytest.mark.parametrize('name, meta_tag, model', [('Database_prod', 'DB_Tag', 'database_model')])
def test_delete_product_from_database(browser_driver, get_url, open_admin_dashboard, name, meta_tag, model):
    """Test for delete test product"""
    # Adding new product
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)

    # Delete product
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .remove_element()
    Alert(browser_driver).accept()
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)

    sql_query = 'SELECT * FROM oc_product WHERE model="database_model"'

    assert not getDatabaseQuery(sql_query)
