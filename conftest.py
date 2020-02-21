"""Fixtures for start different browsers"""
import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage

# Change working directory for open config file
os.chdir(os.path.dirname(__file__))
config_path = os.path.abspath('config.json')
print(config_path)

# Open config file and getting values
with open(config_path) as config_file:
    json_data = json.load(config_file)

admin_name = json_data['username']
password = json_data['password']


def pytest_addoption(parser):
    """Parser for command line parameters"""
    parser.addoption('--url',
                     action='store',
                     default='http://127.0.0.1/opencart/admin/',
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
    wait = WebDriverWait(browser_driver, 7)
    open_link = browser_driver.get(url)
    browser_driver.implicitly_wait(40)
    return open_link


@pytest.fixture()
def open_admin_dashboard(browser_driver):
    """Fixture for login to Admin panel"""
    username_input = browser_driver.find_element(*LoginPage.USERNAME_INPUT)
    username_input.send_keys(admin_name)
    password_input = browser_driver.find_element(*LoginPage.PASSWORD_INPUT)
    password_input.send_keys(password)
    browser_driver.find_element(*LoginPage.LOGIN_BUTTON).click()


