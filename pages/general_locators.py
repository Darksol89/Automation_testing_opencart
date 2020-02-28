"""Different selectors for General page"""
from selenium.webdriver.common.by import By


class GeneralSelectors:
    OPEN_LOGIN_PAGE = (By.XPATH, "//div[@class='col-sm-3']//a[text()='My Account']")
    OPEN_WISH_LIST = (By.XPATH, "//div[@class='col-sm-3']//a[text()='Wish List']")
    OPEN_TABLETS_CATALOG_PAGE = (By.XPATH, "//li[a='Tablets']")
    OPEN_SOFTWARE_CATALOG_PAGE = (By.XPATH, "//li[a='Software']")
    OPEN_CAMERAS_CATALOG_PAGE = (By.XPATH, "//li[a='Cameras']")
    OPEN_SEARCH_PAGE = (By.CSS_SELECTOR, '.input-group-btn')
    OPEN_SHOPPING_CART_PAGE = (By.XPATH, "//div[@id='top-links']//a[@title='Shopping Cart']")
    OPEN_CHECKOUT_PAGE = (By.XPATH, "//div[@id='top-links']//a[@title='Checkout']")
    OPEN_MACBOOK_PRODUCT_PAGE = (By.XPATH, "//div[@class='product-thumb transition']//a[text()='MacBook']")
    OPEN_IPHONE_PRODUCT_PAGE = (By.XPATH, "//div[@class='product-thumb transition']//a[text()='iPhone']")
