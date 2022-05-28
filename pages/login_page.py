from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "The URL doesn't contain 'login' substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The register form is not found"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON).click()
        assert self.is_element_present(*LoginPageLocators.SUCCESS_SIGN_UP_ALERT)
        success_alert_mess = self.browser.find_element(*LoginPageLocators.SUCCESS_SIGN_UP_ALERT).text
        assert "Thanks for registering!" in success_alert_mess, "The user has not been registered."




