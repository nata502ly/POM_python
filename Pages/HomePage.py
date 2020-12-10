from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    HEADER = (By.CSS_SELECTOR, 'h2')
    ALERT = (By.CSS_SELECTOR, 'div.flash.success')
    LOGOUT_BTN = (By.CSS_SELECTOR, 'a[href="/logout"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_logout_button_exist(self):
        return self.is_visible(self.LOGOUT_BTN)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_alert_value(self):
        if self.is_visible(self.ALERT):
            return self.get_element_text(self.ALERT)

    def do_close_browser(self):
        self.close_browser()
