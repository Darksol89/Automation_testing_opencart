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
        SAVE_PRODUCT = (By.CSS_SELECTOR, "button[data-original-title='Save']")
        CANCEL_PRODUCT = (By.CSS_SELECTOR, "a[data-original-title='Cancel']")
        PRODUCT_3 = (By.XPATH, "//table[@class='table table-bordered table-hover']//input[@value='30']")
        PRODUCT_51 = (By.XPATH, "//table[@class='table table-bordered table-hover']//input[@value='54']")
        SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Success: You have modified products!')]")

    class ProductForm:
        PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
        META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
        PRODUCT_TAG = (By.CSS_SELECTOR, '#input-tag1')