import time
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver



class PimPage(BaseDriver):
    def __init__(self, driver,logger):
        super().__init__(driver)
        self.logger=logger
    pim  =(By.XPATH,"//*[@class='oxd-main-menu']//li[2]//span//parent::a")
    add_employee = (By.XPATH,"//a[contains(text(),'Add Employee')]")
    first_name = (By.XPATH,"//input[@name='firstName']")
    middle_name = (By.XPATH, "//input[@name='middleName']")
    last_name = (By.XPATH, "//input[@name='lastName']")
    employee_id = (By.XPATH, "//label[@class='oxd-label']/parent::div/following-sibling::div//input")
    save_button= (By.XPATH,"//button[@type='submit']")
    employee_list_tab=(By.XPATH,"//a[contains(text(),'Employee List')]")
    employee_name_search = (By.XPATH,"//label[contains(text(),'Employee Name')]//parent::div/following-sibling::div//input")
    employee_id_search = (By.XPATH, "//label[contains(text(),'Employee Id')]//parent::div/following-sibling::div//input")
    search_button = (By.XPATH,"//button[@type='submit']")
    employee_available = (By.XPATH,"//*[@class='oxd-table-body']/div")
    def clic_on_pim(self):
        self.logger.info(f" clicking on PIM")
        self.click_on_element(self.pim)
    def click_on_add_employee(self):
        self.logger.info(f" clicking on add employee")
        self.click_on_element(self.add_employee)

    def fill_employee_details(self,first_name,middle_name,last_name,employee_id):
        self.logger.info(f" entering first name")
        time.sleep(10)
        self.enter_text(self.first_name,first_name)
        self.logger.info(f" entering middle name")
        time.sleep(10)
        self.enter_text(self.middle_name, middle_name)
        self.logger.info(f" entering last name")
        time.sleep(10)
        self.enter_text(self.last_name, last_name)
        self.logger.info(f" entering employee id")
        time.sleep(10)
        self.enter_text(self.employee_id, employee_id)
        self.logger.info(f" all employee details entered")
    def save_employee_details(self):
        self.logger.info(f" clicking on save ")
        self.click_on_element(self.save_button)

    def is_employee_added(self,first_name,employee_id):
        self.logger.info(f" fetch the added employee details")
        time.sleep(10)
        self.click_on_element(self.employee_list_tab)
        time.sleep(10)
        self.enter_text(self.employee_name_search, first_name)
        time.sleep(10)
        #self.enter_text(self.employee_id_search, employee_id)
        time.sleep(2)
        self.logger.info(f" clicking on search")
        self.click_on_element(self.search_button)
        try:
            self.logger.info("checking for added Employee details")
            time.sleep(2)
            self.find_element(self.employee_available)
            self.logger.info(f"successfully got the added employee details")
            return True

        except Exception as e:
            self.logger.error(f" failed to fetch the added employee details {e}")
            return False


