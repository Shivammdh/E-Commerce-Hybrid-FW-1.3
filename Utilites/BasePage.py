from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



class BaseClass:
    def __init__(self,driver):
        self.driver=driver
    def verifywait(self,By_locator,locator_value):
        self.locator=By_locator
        flwait = WebDriverWait(self.driver, timeout=30, poll_frequency=5, ignored_exceptions=[NoSuchElementException])
        return flwait.until(EC.presence_of_element_located((By_locator,locator_value)))

    def selectOptionByValue(self,locator,value):
        sel = Select(locator)
        sel.select_by_value(value)