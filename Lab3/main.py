from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time


def test_successful_login():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys("Admin")
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("admin123")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        dashboard_header = driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-headerbreadcrumb .oxd-text")
        assert dashboard_header.text == "Dashboard"
        user_dropdown = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
        assert user_dropdown.is_displayed()
        print("Тест пройден! Логин выполнен успешно.")
    finally:
        time.sleep(20)
        driver.quit()
if __name__ == "__main__":
    test_successful_login()