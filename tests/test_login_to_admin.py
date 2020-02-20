

def test_login_to_admin_panel(browser_driver, get_url, open_admin_dashboard):
    assert 'Dashboard' == browser_driver.title