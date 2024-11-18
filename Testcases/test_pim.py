import time

from Pages.pim_page import PimPage
from faker import   Faker

fake=Faker()
class Test_Pim_Page():
    def test_add_employee_details(self,setup,logger,login):
        first_name =fake.first_name()
        middle_name = fake.first_name_male()
        last_name = fake.last_name()
        employee_id = fake.random_int(min=1000,max=9999)

        try:

            pim_page= PimPage(setup,logger)
            time.sleep(10)

            time.sleep(10)
            pim_page.clic_on_pim()

            time.sleep(10)
            pim_page.click_on_add_employee()

            time.sleep(10)
            pim_page.fill_employee_details(first_name,middle_name,last_name,employee_id)

            time.sleep(10)
            pim_page.save_employee_details()
            time.sleep(20)
            assert pim_page.is_employee_added(first_name,employee_id), "Failed to add employee"
        except Exception as e:
            logger.error(f"Error adding employee: {str(e)}")
            assert False, "Test failed due to an exception"
