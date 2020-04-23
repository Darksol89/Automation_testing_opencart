"""Fixtures for start different browsers"""
import pytest
import json
import os
import logging
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.LoginPage import LoginPage
from helpers.log_listener import Listener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver

# Change working directory for open config file
os.chdir(os.path.dirname(__file__))
config_path = os.path.abspath('config.json')
print(config_path)

# Open config file and getting values
with open(config_path) as config_file:
    json_data = json.load(config_file)

admin_name = json_data['username']
password = json_data['password']


# Logger with Info message for start and finish browser
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger('Web Driver')

def pytest_addoption(parser):
    """Parser for command line parameters"""
    parser.addoption('--url',
                     action='store',
                     default='http://localhost',
                     help='Main link for Opencart')
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: ie, firefox, chrome')
    parser.addoption('--timeout',
                     action='store',
                     default=40,
                     help='Timeout for wait WebDriver')
    parser.addoption('--file',
                     action='store',
                     default=None,
                     help='Filename with log report')


@pytest.fixture()
def my_logger(request):
    """Custom logger"""
    filename = request.config.getoption('--file')
    logging.basicConfig(level=logging.INFO, filename=filename)
    logger = logging.getLogger('Web Driver')
    if filename == None:
        stdout_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stdout_handler)
    else:
        file_handler = logging.FileHandler(filename)
        logger.addHandler(file_handler)

    return logger


@pytest.fixture()
def browser_driver(request, my_logger):
    """Initializing and open browser"""
    browser = request.config.getoption("--browser_name")
    if browser == 'ie':
        my_logger.info('\nStart Internet Explorer browser for test...')
        browser = webdriver.Ie()
    elif browser == 'chrome':
        my_logger.info('\nStart Chrome browser for test...')
        d = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('--ignore-certificate-errors')
        d['loggingPrefs'] = {'browser': 'ALL'}
        browser = webdriver.Chrome(desired_capabilities=d, options=options)
    elif browser == 'firefox':
        my_logger.info('\nStart Firefox browser for test...')
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        browser = webdriver.Firefox(options=options)
        browser = EventFiringWebDriver(webdriver.Firefox(options=options), Listener())
    yield browser
    browser_log = browser.get_log('browser')
    if 'ERROR' in browser_log:
        my_logger.info('Error in browser log')
    my_logger.info('\nClose browser...')
    browser.quit()


@pytest.fixture()
def get_url(request, browser_driver):
    """Fixture for get link from parameter"""
    url = request.config.getoption("--url")
    timeout = request.config.getoption('--timeout')
    wait = WebDriverWait(browser_driver, 7)
    open_link = browser_driver.get(url)
    browser_driver.implicitly_wait(timeout)

    return open_link


@pytest.fixture()
def open_admin_dashboard(browser_driver):
    """Fixture for login to Admin panel"""
    username_input = browser_driver.find_element(*LoginPage.USERNAME_INPUT)
    username_input.send_keys(admin_name)
    password_input = browser_driver.find_element(*LoginPage.PASSWORD_INPUT)
    password_input.send_keys(password)
    browser_driver.find_element(*LoginPage.LOGIN_BUTTON).click()
