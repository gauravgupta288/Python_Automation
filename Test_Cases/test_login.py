from Page_Objects.Login_Page import LoginPage
import logging


class TestLogin:
    loginPage = LoginPage()

    # Test case to validate login
    def test_login(self):
        logging.debug("Login test started")
        self.loginPage.login()
