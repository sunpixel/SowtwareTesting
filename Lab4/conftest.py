import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")
    yield driver
    driver.quit()

@pytest.fixture
def form_page(driver):
    from pagetest import PracticeFormPage
    return PracticeFormPage(driver)