"""Selectors for different elements in the Opencart admin page """
from selenium.webdriver.common.by import By


class AdminDashboard:
    class Navigation:
        CATALOG = (By.XPATH, '//li[@id="menu-catalog"]/a[contains(text(), "Catalog")]')
        CATALOG_PRODUCTS = (By.XPATH, '//ul[@id="collapse1"]/li[2]/a[contains(text(), "Products")]')
    class Products:
        ADD_NEW = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
        EDIT = (By.CSS_SELECTOR, "a[data-original-title='Edit']")
        REMOVE = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
        SAVE_NEW_PRODUCT = (By.CSS_SELECTOR, "button[data-original-title='Save']")
        CANCEL_NEW_PRODUCT = (By.CSS_SELECTOR, "a[data-original-title='Cancel']")
        PRODUCT_APPLE = (By.XPATH, "//table[@class='table table-bordered table-hover']//input[@value='42']")