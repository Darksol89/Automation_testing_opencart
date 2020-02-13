"""Selectors for different elements in the Opencart main page """
from selenium.webdriver.common.by import By


class Selectors:
    swiper_head = (By.CSS_SELECTOR, '.swiper-viewport #slideshow0')
    swiper_footer = (By.CSS_SELECTOR, '.swiper-viewport #carousel0')
    featured_header = (By.CSS_SELECTOR, 'h3')
    button_group = (By.CSS_SELECTOR, '.button-group')
    swiper_buttons = (By.CSS_SELECTOR, '.swiper-pager .swiper-button-next')
