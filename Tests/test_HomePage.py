from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestHome(BaseTest):

    def setup(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASS)

    def test_home_page_title(self):
        title = self.homePage.get_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE

    def test_home_page_header(self):
        header = self.homePage.get_header_value()
        assert header == TestData.HOME_HEADER

    def test_alert(self):
        alert = self.homePage.get_alert_value()
        assert TestData.ALERT in alert

    def test_logout_btn_exist(self):
        self.homePage.is_logout_button_exist()
