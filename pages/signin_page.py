from .base_page import BasePage
from locators import LoginLocators


class SigninPage(BasePage):

    def go_login(self):
        self.click_with_wait(LoginLocators.LOGIN_BUTTON)

    def go_logout(self):
        self.click_with_wait(LoginLocators.LOGOUT_BUTTON)

    def login(self, email, password):
        self.wait_for_overlay(LoginLocators.EMAIL)
        self.input_text(LoginLocators.EMAIL, email)
        self.input_text(LoginLocators.PASSWORD, password)
        self.click_with_wait(LoginLocators.SUBMIT_BUTTON)
        self.handle_login_alert_and_reload(LoginLocators.LOGIN_ERROR_ALERT)

    def new_register(self):
        self.wait_for_overlay(LoginLocators.EMAIL)
        self.click(LoginLocators.REGISTER_BUTTON)

    def check_elem_logout(self):
        self.wait_for_overlay(LoginLocators.LOGOUT_BUTTON)
        if not self.is_element_visible(LoginLocators.LOGOUT_BUTTON):
            return False
        else:
            return True
