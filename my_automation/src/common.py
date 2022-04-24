from .browser_action import BrowserAction
from .locators import *
from .amazon_search import amazon_search

class common(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.g_obj = amazon_search(driver)

    def launch_url(self, url):
        self.driver.get(url)
        print("test")