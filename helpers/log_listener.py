"""logger listener"""
import logging
from selenium.webdriver.support.events import AbstractEventListener

logging.basicConfig(level=logging.INFO, filename='report.log')
logger = logging.getLogger('Browser actions')


class Listener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        logger.info(f"I'm navigating to {url}")

    def after_navigate_to(self, url, driver):
        logger.info(f"I'm on {url}")

    def before_navigate_back(self, driver):
        logger.info(f"I'm navigating back")

    def after_navigate_back(self, driver):
        logger.info(f"I'm back!")

    def before_find(self, by, value, driver):
        logger.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        logger.info(f"I've found '{value}' with '{by}'")

    def before_execute_script(self, script, driver):
        logger.info(f"I'm executing '{script}'")

    def after_execute_script(self, script, driver):
        logger.info(f"I've executed '{script}'")

    def before_quit(self, driver):
        logger.info(f"I'm getting ready to terminate {driver}")

    def after_quit(self, driver):
        logger.info(f"WASTED!!!")

    def on_exception(self, exception, driver):
        logger.error(f'Oooops i got: {exception}')
        driver.save_screenshot(f'{exception}.png')
