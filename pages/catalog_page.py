"""Selectors for different elements in the Opencart catalog page """
from selenium.webdriver.common.by import By


class CatalogPage:
    LIST_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_BUTTON = (By.CSS_SELECTOR, 'grid-view')
    SORT_BY = (By.XPATH, '//select[@id="input-sort"]')
    SHOW_COMBOBOX = (By.XPATH, "//select[@id='input-limit']")
    PRODUCT_LIST = (By.CSS_SELECTOR, '.list-group')
