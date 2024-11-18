
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:

    def __init__(self,driver):
        self.driver = driver
        self.timeout=10


    def find_element(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(locator))

    def find_elements(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_all_elements_located(locator))

    def click_on_element(self,locator):
        element =  WebDriverWait(self.driver,self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self,locator,text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.find_element(locator).text


    def get_title(self):

        return self.driver.title