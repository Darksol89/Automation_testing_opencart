"""Fixtures for start different browsers"""
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Parser for command line parameters"""
    parser.addoption('--url',
                     action='store',
                     default='http://127.0.0.1/opencart/',
                     help='Main link for Opencart')
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: ie, firefox, chrome')


@pytest.fixture()
def browser_driver(request):
    """Initializing and open browser"""
    browser = request.config.getoption("--browser_name")
    if browser == 'ie':
        print('\nStart Internet Explorer browser for test...')
        browser = webdriver.Ie()
    elif browser == 'chrome':
        print('\nStart Chrome browser for test...')
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        browser = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        print('\nStart Firefox browser for test...')
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        browser = webdriver.Firefox(options=options)
    yield browser
    print('\nClose browser...')
    browser.quit()


@pytest.fixture()
def get_url(request, browser_driver):
    """Fixture for get link from parameter"""
    url = request.config.getoption("--url")
    open_link = browser_driver.get(url)
    browser_driver.implicitly_wait(40)
    return open_link
