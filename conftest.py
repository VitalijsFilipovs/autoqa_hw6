import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os

@pytest.fixture
def driver():
    options = Options()
    options.headless = False

    # Явный путь к geckodriver.exe в корне проекта
    driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "geckodriver.exe"))
    service = Service(executable_path=driver_path)

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
