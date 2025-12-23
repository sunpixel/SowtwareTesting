from selenium.webdriver.common.by import By
from basepage import BasePage

class PracticeFormPage(BasePage):

    # Locators
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[contains(.,'Male')]")
    GENDER_FEMALE = (By.XPATH, "//label[contains(.,'Female')]")
    GENDER_OTHER = (By.XPATH, "//label[contains(.,'Other')]")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.XPATH, "//label[contains(.,'Sports')]")
    HOBBIES_READING = (By.XPATH, "//label[contains(.,'Reading')]")
    HOBBIES_MUSIC = (By.XPATH, "//label[contains(.,'Music')]")
    UPLOAD_PICTURE = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    SUBMIT_BUTTON = (By.ID, "submit")
    # Modal after submission
    SUCCESS_MODAL = (By.CLASS_NAME, "modal-content")
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    STUDENT_NAME = (By.XPATH, "//td[text()='Student Name']/following-sibling::td")
    STUDENT_EMAIL = (By.XPATH, "//td[text()='Student Email']/following-sibling::td")
    STUDENT_MOBILE = (By.XPATH, "//td[text()='Mobile']/following-sibling::td")
    # Error fields
    FIRST_NAME_ERROR = (By.ID, "firstName-helper-text")
    EMAIL_ERROR = (By.ID, "userEmail-helper-text")

    def enter_first_name(self, first_name):
        self.find_clickable_element(self.FIRST_NAME).clear()
        self.find_clickable_element(self.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_clickable_element(self.LAST_NAME).clear()
        self.find_clickable_element(self.LAST_NAME).send_keys(last_name)

    def enter_email(self, email):
        self.find_clickable_element(self.EMAIL).clear()
        self.find_clickable_element(self.EMAIL).send_keys(email)

    def select_gender(self, gender="Male"):
        if gender.lower() == "female":
            self.find_clickable_element(self.GENDER_FEMALE).click()
        elif gender.lower() == "other":
            self.find_clickable_element(self.GENDER_OTHER).click()
        else:
            self.find_clickable_element(self.GENDER_MALE).click()

    def enter_mobile(self, mobile):
        self.find_clickable_element(self.MOBILE).clear()
        self.find_clickable_element(self.MOBILE).send_keys(mobile)

    def enter_address(self, address):
        self.find_clickable_element(self.CURRENT_ADDRESS).clear()
        self.find_clickable_element(self.CURRENT_ADDRESS).send_keys(address)

    def submit_form(self):
        self.find_clickable_element(self.SUBMIT_BUTTON).click()

    def is_success_modal_displayed(self):
        return self.is_element_visible(self.SUCCESS_MODAL)

    def get_success_message(self):
        return self.get_element_text(self.MODAL_TITLE)

    def get_student_name(self):
        return self.get_element_text(self.STUDENT_NAME)

    def is_first_name_error_displayed(self):
        return self.is_element_visible(self.FIRST_NAME_ERROR)

    def get_first_name_error_text(self):
        return self.get_element_text(self.FIRST_NAME_ERROR)

    def get_student_email(self):
        return self.get_element_text(self.STUDENT_EMAIL)

    def get_student_mobile(self):
        return self.get_element_text(self.STUDENT_MOBILE)

    def close_success_modal(self):
        """Close the success modal by clicking outside or close button if available"""
        # Try to find and click a close button if it exists
        try:
            close_button = self.driver.find_element(By.CLASS_NAME, "close")
            close_button.click()
        except:
            # If no close button, click outside the modal
            modal = self.find_clickable_element(self.SUCCESS_MODAL)
            modal.click()