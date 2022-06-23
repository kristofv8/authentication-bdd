from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.utils import report_message_log, soft_verify_data


class AdminMainPage(BasePage):
    LOCATORS = {
        "header": (By.ID, "user-tools"),
        "invoices_link": (By.LINK_TEXT, "Invoices"),
        "forgot_password_link": (By.LINK_TEXT, "CHANGE PASSWORD"),
        "logout_link": (By.LINK_TEXT, "LOG OUT"),
    }

    def __init__(self, context):
        super().__init__(context)
        self.login_data = context.data['login_data']

    def verify_header(self):
        self.wait_to_visible(self.LOCATORS['header'])
        header_text = self.find_elements(*self.LOCATORS['header']).text
        response = soft_verify_data(header_text, self.login_data['user']['username'], "User is able to see the client username")

        if not response:
            report_message_log("User not able to see the client username")

    def click_forgot_password_link(self):
        self.find_elements(*self.LOCATORS['forgot_password_link']).click()
