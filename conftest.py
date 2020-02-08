"""Fixtures for start different browsers"""
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Parser for command line parameters"""
    parser.addoption('--url',
                     action='store',
                     default='http://192.168.1.232/opencart/',
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
        options = webdriver.IeOptions()
        driver_options(options)
        browser = webdriver.Ie(options=options)
        browser.implicitly_wait(40)
    elif browser == 'chrome':
        print('\nStart Chrome browser for test...')
        options = webdriver.ChromeOptions()
        driver_options(options)
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(40)
    elif browser == 'firefox':
        print('\nStart Firefox browser for test...')
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        # driver_options(options)
        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(40)
    yield browser
    print('\nClose browser...')
    browser.quit()


@pytest.fixture()
def get_url(request, browser_driver):
    """Fixture for get link from parameter"""
    url = request.config.getoption("--url")
    open_link = browser_driver.get(url)
    return open_link


def driver_options(options):
    options.add_argument("headless")
