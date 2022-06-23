from behave import then, step
from selenium.common.exceptions import TimeoutException
from pages.admin_main_page import AdminMainPage


@then("user should be able to see admin main page")
def verify_admin_main_header(context):
    page = AdminMainPage(context)
    page.verify_header()


@then('user should be able to "{URL_NAME}"')
def verify_user_should_open_all_pages(context, URL_NAME):
    app_url = f"{context.data['url']}{URL_NAME}"
    try:
        context.driver.get(app_url)
    except TimeoutException as e:
        print('f{app_url}')


@step("user clicks on the invoices link")
def click_invoices_link(context):
    page = AdminMainPage(context)
    page.click_invoices_link()


@step("user clicks on the to be shipped link")
def click_to_be_shipped_link(context):
    page = AdminMainPage(context)
    page.click_to_be_shipped_link()


@step("user clicks on the logout link")
def click_logout_link(context):
    page = AdminMainPage(context)
    page.click_on_logout()
