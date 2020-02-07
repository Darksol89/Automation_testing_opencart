"""Test for open main page Opencart web site"""


def test_open_site(browser_driver, get_url):
    assert 'Google' == browser_driver.title
