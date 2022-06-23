import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from pages.utils import report_message_log


class BaseFilter:
    def __init__(self, driver):
        self.driver = driver

    def select_option(self, section_name, link_text):
        changelist_filter = self.driver.find_element_by_id('changelist-filter')
        filter_section = changelist_filter.find_element_by_xpath(f"//h3[contains(text(), '{section_name}')]/following-sibling::ul")
        link_by_text = filter_section.find_element_by_link_text(link_text)
        link_by_text.click()


class BasePage:
    DEFAULT_WAIT_TIMEOUT = 3

    def __init__(self, context):
        self.data = context.data
        self.driver = context.driver
        self.result_list_xpath = '//*[@id="result_list"]/tbody/tr[1]'
        self.button_save_xpath = '//*[@id="result_list"]/tbody/tr[1]/td[1]/button'

    def get_first_row_from_table_and_mark_checkbox(self, field_name):
        first_row_in_result_table = self.driver.find_element_by_xpath(self.result_list_xpath)
        first_order_id = first_row_in_result_table.find_element_by_class_name(field_name).text
        input_checkbox = first_row_in_result_table.find_element_by_class_name('action-select')
        input_checkbox.click()
        return first_order_id

    def click_go(self):
        self.driver.find_element_by_name('index').click()

    def select_admin_action(self, action_name):
        auto_select = Select(self.driver.find_element_by_tag_name("select"))
        auto_select.select_by_visible_text(action_name)

    def find_elements(self, *element):
        return self.driver.find_element(*element)

    def navigate_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)

    def wait_to_visible(self, element):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located(element))
        except TimeoutException:
            report_message_log("Loading takes too much time")

    def switch_to_frame(self, element):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it(element))
        except TimeoutException:
            report_message_log("Loading takes too much time")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def report_screenshot_log(self, message):
        allure.attach(self.driver.get_screenshot_as_png(), name=message)

    def refresh_page(self):
        self.driver.refresh()

    def switch_to_new_window(self):
        current_window_name = self.driver.current_window_handle
        window_names = self.driver.window_handles
        for window in window_names:
            if window != current_window_name:
                self.driver.switch_to.window(window)

    def switch_to_next_tab(self):
        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])

    def switch_to_alert(self):
        self.driver.switch_to.alert.accept()

    def find_order_id(self, conref_value):
        self.driver.find_element_by_name('q').send_keys(conref_value)
        self.driver.find_element_by_xpath("//*[@id='changelist-search']/div/input[2]").click()

    def click_save_changes(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()

    def set_filters(self, section_name, link_text):
        BaseFilter(self.driver).select_option(section_name, link_text)

    def click_save(self):
        self.driver.find_element_by_name('_save').click()

