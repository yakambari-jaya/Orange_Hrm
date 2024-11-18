import logging
import time
from selenium.webdriver.common.by import By
import pytest
from Pages.login_page import LoginPage
from Testcases.conftest import get_test_data
from Utilities.utils import check_broken_link

@pytest.mark.usefixtures('setup')
class Test_Login_Page():
    username= "Admin"
    password ="admin123"
    invalid_username ="admin123"
    invalid_password ="Admin"
    links_xpath = (By.XPATH,"//a")


    def test_login_with_data_driven(self,setup,logger,get_test_data):
        login_page =LoginPage (setup,logger)
        for credentials in get_test_data:
            try:
                username, password, expected_message =credentials
                time.sleep(5)
                login_page.login(username,password)
                time.sleep(10)
                if expected_message.lower() =="success":
                    assert "dashboard" in setup.current_url.lower(),"** login failed for valid credentials**"
                    login_page.click_logout()
                    logger.info("*******   login successful for valid credentials ********")
                else:
                    error_message =login_page.get_error_message()
                    assert expected_message in error_message,f"Excpeted: {expected_message} but found:{error_message}"
                    logger.info("*******   Error message validated for in valid credentials ********")
            except Exception as e:
                logger.error(f"error during login: {str(e)}")
                assert False,"test failed due to exception"
    def test_homepage_title(self,setup,logger):

        login_obj = LoginPage(setup,logger)
        time.sleep(20)
        logger.info("----****---- Starting HomePage Title Test ----****----")
        page_title = login_obj.homepage_title()

        if page_title == "OrangeHRM":
            logger.info("----****---- HomePage Title Test Pass ----****----")
            assert True
        else:
            logger.error("----****---- HomePage Title Test Fail ----****----")
            assert False


    def test_broken_link_before_login(self,setup,logger):
        logger.info("----****---- Starting broken link Test ----****----")
        a=check_broken_link(setup,self.links_xpath)
        if len(a)>0:
            logger.info("----****---- Starting broken link Test Failed----****----")
            assert False
        else:
            logger.error("----****---- Starting broken link Test Passed----****----")
            assert True


    def test_login_with_invalid_credentials(self,setup,logger):
        logger.info("----****---- Starting Login Test with invalid credentials ----****----")
        login_obj = LoginPage(setup,logger)
        login_obj.enter_username(self.invalid_username)
        login_obj.enter_password(self.invalid_password)
        login_obj.click_login()

        if not login_obj.invalid_credential_msg():
            logger.error("----****----  Invalid Login Test Failed----****----")
            assert False
        else:
            logger.info("----****----  Invalid Login Test Passed----****----")
            assert True

    def test_login_with_valid_credentials(self,setup,logger):
        logger.info("----****---- Starting Login Test ----****----")
        login_obj = LoginPage(setup,logger)
        login_obj.enter_username(self.username)
        login_obj.enter_password(self.password)
        login_obj.click_login()
        assert "dashboard" in setup.current_url.lower(), "** login failed for valid credentials**"
        login_obj.click_logout()
        logger.info("*******   login successful for valid credentials ********")



    def test_logout(self,setup,logger):
        logger.info("----****---- Starting Logout Test ----****----")
        login_obj = LoginPage(setup, logger)
        login_obj.enter_username(self.username)
        login_obj.enter_password(self.password)
        login_obj.click_login()
        logout_status = login_obj.click_logout()
        if logout_status:
            logger.info("----****---- Logout Test passed----****----")
            assert True
        else:
            logger.error("----****---- Logout Test Failed----****----")
            assert False