import pytest

class TestPracticeFormPositive:
    def test_successful_form_submission(self, form_page):
        """Позитивный тест: заполнение всех полей валидными данными"""
        # Fill required fields
        form_page.enter_first_name("Иван")
        form_page.enter_last_name("Петров")
        form_page.enter_email("ivan.petrov@example.com")
        form_page.select_gender("Male")
        form_page.enter_mobile("1234567890")
        form_page.enter_address("Москва, ул. Примерная, д. 123")
        form_page.submit_form()
        
        # Verify successful submission
        assert form_page.is_success_modal_displayed(), "Модальное окно успеха не отображается"
        
        # Get modal text and verify content
        success_text = form_page.get_success_message()
        assert "Thanks for submitting the form" in success_text, f"Неверное сообщение об успехе. Получено: {success_text}"
        
        # Verify student name in results
        student_name = form_page.get_student_name()
        assert "Иван Петров" in student_name, f"Неверное имя студента в результатах. Получено: {student_name}"
        
        # Close modal after verification
        form_page.close_success_modal()

class TestPracticeFormNegative:
    def test_empty_required_field_submission(self, form_page):
        """Негативный тест: отправка формы с пустым обязательным полем"""
        # Fill all fields except first name (required)
        form_page.enter_last_name("Петров")
        form_page.enter_email("ivan.petrov@example.com")
        form_page.select_gender("Male")
        form_page.enter_mobile("1234567890")
        form_page.enter_address("Москва, ул. Примерная, д. 123")
        form_page.submit_form()
        
        # Form should not submit successfully
        assert not form_page.is_success_modal_displayed(), "Модальное окно успеха не должно отображаться при ошибке"
        
        # Verify page didn't redirect and form is still visible
        assert "automation-practice-form" in form_page.driver.current_url, "Страница формы не осталась активной"
        
        # Optional: Verify first name field shows validation error
        if hasattr(form_page, 'is_field_in_error_state'):
            assert form_page.is_field_in_error_state("firstName"), "Поле 'Имя' должно показывать ошибку валидации"

    def test_invalid_email_format(self, form_page):
        """Негативный тест: неверный формат email"""
        form_page.enter_first_name("Иван")
        form_page.enter_last_name("Петров")
        form_page.enter_email("invalid-email")  # Invalid format
        form_page.select_gender("Male")
        form_page.enter_mobile("1234567890")
        form_page.enter_address("Москва, ул. Примерная, д. 123")
        form_page.submit_form()
        
        # Form should not submit with invalid email
        assert not form_page.is_success_modal_displayed(), "Форма не должна отправляться с неверным email"
        
        # Verify page didn't redirect
        assert "automation-practice-form" in form_page.driver.current_url, "Страница формы не осталась активной"
        
        # Optional: Check for email validation error
        if hasattr(form_page, 'is_email_validation_error_visible'):
            assert form_page.is_email_validation_error_visible(), "Должна отображаться ошибка валидации email"