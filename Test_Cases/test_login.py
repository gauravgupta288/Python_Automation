from Page_Objects.Login_Page import LoginPage
import pytest
import logging


class TestLogin:
    username = "admin@yourstore.com"
    password = "admin"

    loginPage = LoginPage()
    logger = logging.getLogger()
    fhandler = logging.FileHandler(filename='Logs/mylog.log', mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.DEBUG)

    # Test case to validate login
    def test_login(self):
        logging.debug("Login test started")
        self.loginPage.login(self.username, self.password)
