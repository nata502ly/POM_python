from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, 'input#username')
    PASS = (By.CSS_SELECTOR, 'input#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SELENIUM_LINK = (By.CSS_SELECTOR, 'a[href="http://elementalselenium.com/"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_selenium_link_exist(self, text):
        assert self.get_element_text(self.SELENIUM_LINK) == text

    def do_login(self, username, password):
        self.driver.get(f'{TestData.BASE_URL}/login')
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASS, password)
        self.do_click(self.LOGIN_BUTTON)
