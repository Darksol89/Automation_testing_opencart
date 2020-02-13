"""Selectors for different elements in the Opencart main page """
from selenium.webdriver.common.by import By


class MainPage:
    PROMOBLOCK_HEAD = (By.CSS_SELECTOR, '.swiper-viewport #slideshow0')
    PROMOBLOCK_FOOTER = (By.CSS_SELECTOR, '.swiper-viewport #carousel0')
    PRODUCT_HEADER = (By.CSS_SELECTOR, 'h3')
    BUTTON_GROUP = (By.CSS_SELECTOR, '.button-group')
    PROMOBLOCK_NAV_BUTTON = (By.CSS_SELECTOR, '.swiper-pager .swiper-button-next')
