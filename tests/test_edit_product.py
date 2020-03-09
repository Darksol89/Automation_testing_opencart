import pytest
from helpers.page_helpers import wait_for_element
from PageObject.AdminDashPage import AdminDashboard


@pytest.mark.parametrize('name, meta_tag, model', [('Edit_Product', 'Edit_Tag', 'Edit_Model')])
def test_edit_product(browser_driver, get_url, open_admin_dashboard, name, meta_tag, model):
    """Test for Edit one of product"""
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .edit_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()

    # Check result
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()
