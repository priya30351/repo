class BrowserAction:
    def __init__(self, driver):
        self.driver = driver

    def input_text(self, selector, value):
        #driver.find_element_by_css_selector("input#billname").send_keys("priya")

        self.driver.find_element_by_css_selector(selector).send_keys(value)

    def click_element(self, selector):
       # self.driver.find_element_by_xpath(selector)
       self.driver.find_element_by_css_selector(selector).click()