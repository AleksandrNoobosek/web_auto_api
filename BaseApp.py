
import logging
import yaml
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    base_url = testdata['address']

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), 
                                                      message=f"Can't find element by locator{locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element 
    
    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element: # element will be converted to boolean type . And if it is not None, False - the element is found.
            return element.value_of_css_property(property)
        logging.error(f"Proprty {property} not found in element with locator {locator}")
        return None
    
    def go_to_site(self):
        try:
            start_browser = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site") 
            start_browser = None
        return start_browser

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None
        
        
        
        
        