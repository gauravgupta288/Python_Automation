from  Page_Objects.Login_Page import Login_Page
from selenium import webdriver
import pytest
class Test_Login_TC001:
    username = "admin@yourstore.com"
    password = "admin"
    url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"

    #Test case to validate login
    def test_login(self):
        driver = webdriver.chrome()
        driver.get(self.url)
        Login_Page.Login(self.username, self.password)