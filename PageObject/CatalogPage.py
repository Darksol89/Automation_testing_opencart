"""Selectors for different elements in the Opencart catalog page """
from selenium.webdriver.common.by import By
from PageObject.GeneralLocators import GeneralSelectors
from PageObject.BasePage import BasePage


class CatalogPage(BasePage):
    LIST_BUTTON = (By.XPATH, '//button[@id="list-view"]')
    LIST_VIEW = (By.XPATH, '//div[@class="product-layout product-list col-xs-12"]')
    GRID_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    GRID_VIEW = (By.XPATH, '//div[@class="product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12"]')
    SORT_BY_COMBOBOX = (By.XPATH, '//select[@id="input-sort"]')
    SORT_BY_SELECTED = (By.XPATH, '//select[@id="input-sort"]/option[@selected]')
    SHOW_COMBOBOX = (By.XPATH, "//select[@id='input-limit']")
    SHOW_VALUE_SELECTED = (By.XPATH, "//select[@id='input-limit']/option[@selected]")
    PRODUCT_TREE = (By.CSS_SELECTOR, '.list-group')

    def open_catalog_page(self):
        self._click_to_element(GeneralSelectors.OPEN_TABLETS_CATALOG_PAGE)
        return self

    def list_button_active(self):
        self._click_to_element(self.LIST_BUTTON)
        self._wait_for_visible(self.LIST_VIEW)
        return self

    def grid_button_active(self):
        self._click_to_element(self.GRID_BUTTON)
        self._wait_for_visible(self.GRID_VIEW)
        return self

    def select_from_sort_by(self, option):
        self._selecting_by_visible_text(self.SORT_BY_COMBOBOX, option)
        self._wait_for_visible(self.SORT_BY_SELECTED)
        return self

    def select_show_element(self, option):
        self._selecting_by_visible_text(self.SHOW_COMBOBOX, option)
        return self

    def verify_product_tree(self):
        self.browser.find_element(*self.PRODUCT_TREE)
        return self
