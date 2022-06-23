from selenium.webdriver.common.by import By

from pages import consts
from pages.base_page import BasePage
from pages.utils import hard_verify_data


class LoginPage(BasePage):
    LOCATORS = {
        "username": (By.ID, "id_username"),
        "password": (By.ID, "id_password"),
        "login_button": (By.XPATH, "//input[@type='submit']"),
        "logout_text": (By.XPATH, "//*[@id='content']/p[1]"),
        "error_message": (By.CLASS_NAME, "errornote"),
    }

    def __init__(self, context):
        super().__init__(context)
        self.login_data = context.data['login_data']

    def login_to_admin(self):
        self.send_client_login_data()
        self.click_login_button()

    def click_login_button(self):
        self.find_elements(*self.LOCATORS['login_button']).click()

    def send_client_login_data(self):
        self.find_elements(*self.LOCATORS['username']).send_keys(self.login_data['user']['username'])
        self.find_elements(*self.LOCATORS['password']).send_keys(self.login_data['user']['password'])

    def verify_login_page(self):
        login_button_text = self.driver.find_element_by_xpath("//span[text()='LOG IN']").text
        hard_verify_data(login_button_text, consts.LOGIN_BUTTON_TEXT, "User is able to login successfully")

    def verify_logout_page(self):
        logout_text = self.find_elements(*self.LOCATORS['logout_text']).text
        hard_verify_data(logout_text, 'Thanks for spending some quality time with the Web site today.', "User is able to logout successfully")

    def send_invalid_username_data(self):
        self.find_elements(*self.LOCATORS['username']).send_keys(self.login_data['user']['invalid_username'])
        self.find_elements(*self.LOCATORS['password']).send_keys(self.login_data['user']['password'])

    def verify_error_message(self):
        error_text = self.find_elements(*self.LOCATORS['error_message']).text
        hard_verify_data(error_text, consts.ERROR_MESSAGE, "User is able to see the error message")

    def send_invalid_password_data(self):
        self.find_elements(*self.LOCATORS['username']).send_keys(self.login_data['user']['username'])
        self.find_elements(*self.LOCATORS['password']).send_keys(self.login_data['user']['invalid_password'])
