from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        assert "login" in current_url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_address.send_keys(email)
        new_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        new_password.send_keys(password)
        new_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        new_password_confirm.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
