from behave import given, then, step

from pages.login_page import LoginPage


@given("user opens the website")
def open_website(context):
    pass


@step("user enters the user username and password")
def client_username_password(context):
    page = LoginPage(context)
    page.send_client_login_data()


@step("user clicks on the login button")
def click_login_button(context):
    page = LoginPage(context)
    page.click_login_button()


@then("user should see the login page")
def verify_login_page(context):
    page = LoginPage(context)
    page.verify_login_page()


@then("user should see the logout page")
def verify_logout_page(context):
    page = LoginPage(context)
    page.verify_logout_page()


@step("user enters the invalid username and password")
def send_invalid_username(context):
    page = LoginPage(context)
    page.send_invalid_username_data()


@then("user should be able to see the error message")
def verify_error_message(context):
    page = LoginPage(context)
    page.verify_error_message()


@step("user enters the username and invalid password")
def send_invalid_password(context):
    page = LoginPage(context)
    page.send_invalid_password_data()
