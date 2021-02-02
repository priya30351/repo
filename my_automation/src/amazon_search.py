from .browser_action import BrowserAction
from .locators import *

class amazon_search(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)


    def search_data_on_google(self, value):
        self.input_text(SEARCH_BOX, value)
        self.click_element(SEARCH_BUTTON)