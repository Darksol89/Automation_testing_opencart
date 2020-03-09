"""Test for adding new option via Admin page"""

from helpers.page_helpers import wait_for_element
from PageObject.AdminDashPage import AdminDashboard


def test_add_new_option(browser_driver, get_url, open_admin_dashboard):
    AdminDashboard(browser_driver) \
        .open_options_from_catalog() \
        .add_new_element() \
        .input_options_form(option_name='Test Option') \
        .add_option_value(value_name='Test Value') \
        .save_element()

    # Check result
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()
