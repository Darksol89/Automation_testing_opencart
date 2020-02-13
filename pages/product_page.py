"""Selectors for different elements in the Opencart product page """
from selenium.webdriver.common.by import By

class ProductPage:
    ADD_TO_CARD = (By.CSS_SELECTOR, '.form-group #button-cart')
    QUANTITY = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_WISH_LIST = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    COMPARE_PRODUCT = (By.XPATH, "//button[@data-original-title='Compare this Product']")
    RATING = (By.CSS_SELECTOR, '.rating')