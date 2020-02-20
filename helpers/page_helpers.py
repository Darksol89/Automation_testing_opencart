from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec

def wait_for_element(browser_driver, locator):
    """Custom waitter different web elements"""
    try:
        WebDriverWait(browser_driver, 5).until(ec.presence_of_element_located(locator))
        browser_driver.implicitly_wait(5)
    except NoSuchElementException:
        print('Web element not found!')
    browser_driver.find_element(*locator)