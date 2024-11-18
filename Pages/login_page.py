import time
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver



class LoginPage(BaseDriver):
    def __init__(self, driver,logger):
        super().__init__(driver)
        self.logger=logger

    username_field =(By.XPATH,"//input[@name='username']")
    password_field = (By.XPATH,"//input[@name='password']")
    login_button = (By.XPATH,"//button[@type='submit']")
    login_failed_msg= (By.XPATH,"//*[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    open_hrm = (By.LINK_TEXT,"OrangeHRM, Inc")
    down_arrow_button =(By.XPATH,"//span[@class='oxd-userdropdown-tab']//i")
    invalid_error_msg = (By.XPATH,"//*[@class='orangehrm-login-error']//*[@role='alert']")
    logout = (By.LINK_TEXT,"Logout")
    home_page_usr_psw_details= (By.XPATH,"//*[@class='orangehrm-login-error']")




    def enter_username(self,username):
        try:
            self.logger.info(f"Entering username")
            self.enter_text(self.username_field,username)
        except Exception as e:
            self.logger.error(f"Failed to Enter username due to {str(e)}")

    def enter_password(self,password):
        try:
            self.logger.info(f"Entering password")
            self.enter_text(self.password_field, password)
        except Exception as e:
            self.logger.error(f"Failed to Enter password due to {str(e)}")

    def click_login(self):
        try:
            self.logger.info(f"Clicking on Login Button")
            self.click_on_element(self.login_button)
        except Exception as e:
            self.logger.error(f"Failed Clicking on Login button due to {str(e)}")



    def click_logout(self):
        try :
            self.logger.info(f"Clicking on down arrow Button")
            time.sleep(2)
            self.click_on_element(self.down_arrow_button)
            self.logger.info(f"Clicking on Logout Button")
            time.sleep(15)
            self.click_on_element(self.logout)
            try:
                time.sleep(5)
                self.find_element(self.home_page_usr_psw_details)
                self.logger.info(f"Logout Successfully")
                return True
            except Exception as e:
                self.logger.error(f"Error in Logout due to {str(e)}")
                return False
        except Exception as e:
            self.logger.error(f"Failed Clicking on Logout due to {str(e)}")


    def homepage_title(self):
        try :
            self.logger.info(f"Getting Homepage title")
            title1 = self.get_title()
            print(f"{title1}dsdsdsd")
            return title1

        except Exception as e:
            self.logger.error(f"Failed to get the title due to {str(e)}")

    def invalid_credential_msg(self):
        try:
            self.logger.info("Getting invalid Credential message present in or not")
            self.find_element(self.invalid_error_msg)
            return True

        except Exception as e:
            self.logger.error(f"Failed to get invalid Credential message present in or not due to {str(e)}")
            return False
    def login(self,username,password):
        self.logger.info(f"logging in using {username},{password}")
        try:
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()
        except Exception as e:
            self.logger.error(f"logging failed in using with {username,password} due to {str(e)}")

    def get_error_message(self):
        try:

            return self.get_text(self.invalid_error_msg)
        except Exception as e:
            return f"Error message not found: {str(e)}"




