from  Page_Objects.Login_Page import LoginPage
from selenium import webdriver
import pytest
class TestLoginTC001:
    username = "admin@yourstore.com"
    password = "admin"
    url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"

    # Test case to validate login
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login_Page()
        Login_Page.Login(self.username, self.password)