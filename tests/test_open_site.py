"""Test for open main page Opencart web site"""


def test_open_site(browser_driver, get_url, my_logger):
    my_logger.info('Open Opencart site')
    assert 'Your Store' == browser_driver.title
