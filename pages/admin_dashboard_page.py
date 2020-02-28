"""Selectors for different elements in the Opencart admin page """
from selenium.webdriver.common.by import By


class AdminDashboard:
    class Navigation:
        CATALOG = (By.XPATH, '//li[@id="menu-catalog"]/a[contains(text(), "Catalog")]')
        CATALOG_PRODUCTS = (By.XPATH, '//ul[@id="collapse1"]/li[2]/a[contains(text(), "Products")]')
    class Products:
        ADD_NEW = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
        EDIT = (By.CSS_SELECTOR, "a[data-original-title='Edit']")
        COPY = (By.CSS_SELECTOR, "button[data-original-title='Copy']")
        REMOVE = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
        SAVE_PRODUCT = (By.CSS_SELECTOR, "button[data-original-title='Save']")
        CANCEL_PRODUCT = (By.CSS_SELECTOR, "a[data-original-title='Cancel']")
        TEST_PRODUCT_FOR_REMOVE = (By.XPATH, "//table//tr[2]/td/input[@type='checkbox']")
        SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Success: You have modified products!')]")


    class ProductForm:
        PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
        META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
        PRODUCT_TAG = (By.CSS_SELECTOR, '#input-tag1')
        MODEL = (By.CSS_SELECTOR, '#input-model')

        class Tabs:
            DATA_TAB = (By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')
