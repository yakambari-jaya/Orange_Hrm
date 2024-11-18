
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Pages.login_page import LoginPage
import pandas as pd
import logging
from datetime import datetime
import pytest




@pytest.fixture( scope="session",autouse=True)
def setup(request,browser):
    if browser=='chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))
        print("Launching Firefox browser")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope="session")
def logger():
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logfile_name = f"Logs/test_execution_{time_stamp}"
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(logfile_name)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    yield logger

@pytest.fixture(scope="session",autouse=False)
def login(setup,logger):
    logger.info("*** loging in using fixture ***")
    login_page =LoginPage(setup,logger)
    login_page.login("Admin","admin123")
    assert "dashboard" in setup.current_url.lower(),"login failed!"
    logger.info("login successfully")
    yield

    login_page.click_logout()


@pytest.fixture()
def get_test_data():
    df = pd.read_csv("Testdata/login_test_data.csv")
    data=[(row['username'],row['password'],row['expected_message']) for _,row in df.iterrows()]
    return data

