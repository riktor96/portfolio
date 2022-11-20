import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(10)
    elif browser_name=="firefox":
        print("There will be firefox")
    else:
        print("There will be IE")
    request.cls.driver = driver
    driver.get("https://empik.pl/")
    yield
    time.sleep(5)
    driver.close()

