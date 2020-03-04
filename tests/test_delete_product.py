from PageObject.AdminDashPage import AdminDashboard
from selenium.webdriver.common.alert import Alert
from helpers.page_helpers import wait_for_element


def test_delete_product(browser_driver, get_url, open_admin_dashboard):
    """Test for delete test product"""
    AdminDashboard(browser_driver) \
        .open_product_from_catalog() \
        .copy_element() \
        .remove_element()
    Alert(browser_driver).accept()
    # Check result
    wait_for_element(browser_driver, AdminDashboard.GeneralActions.SUCCESS_TEXT)
    success_text = browser_driver.find_element(*AdminDashboard.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()
