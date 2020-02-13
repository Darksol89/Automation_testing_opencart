from pages.product_page import ProductPage

def test_product_page(browser_driver, get_url):
    browser_driver.find_element(*ProductPage.ADD_TO_CARD)
    browser_driver.find_element(*ProductPage.ADD_TO_WISH_LIST)
    browser_driver.find_element(*ProductPage.COMPARE_PRODUCT)
    browser_driver.find_element(*ProductPage.QUANTITY)
    browser_driver.find_element(*ProductPage.RATING)