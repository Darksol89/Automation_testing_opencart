"""Selectors for different elements in the Opencart search page """
from selenium.webdriver.common.by import By


class SearchPage:
    OPEN_SEARCH_PAGE = (By.CSS_SELECTOR, '.input-group-btn')
    INPUT_SEARCH = (By.CSS_SELECTOR, '#input-search')
    CATEGORIES_LIST = (By.XPATH, "//select[@name='category_id']")
    CHECKBOX_DESCRIPTION = (By.CSS_SELECTOR, '#description')
    CHECKBOX_SUBCATEGORIES = (By.XPATH, "//input[@name='sub_category']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="button"]')
