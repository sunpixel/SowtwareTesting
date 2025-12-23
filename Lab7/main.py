from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

def main():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Pixel_3a_API_34_extension_level_7_x86_64"
    options.automation_name = "UiAutomator2"

    options.app_package = "com.example.lab_7"
    options.app_activity = ".MainActivity"
    options.no_reset = True

    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)

    try:
        wait = WebDriverWait(driver, 20)

        # ✅ Wait for the button and click it
        heads_up_btn = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "com.example.lab_7:id/btnHeadsUpNotify")
            )
        )
        heads_up_btn.click()
        print("Clicked Heads Up Notify button")

    finally:
        driver.quit()
        print("Session ended.")

if __name__ == "__main__":
    main()
