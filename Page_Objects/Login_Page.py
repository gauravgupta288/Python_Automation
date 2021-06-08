from Page_Objects import Base_Page
from Page_Objects.Base_Page import Base
from selenium import webdriver
from Resources import xmlParser


class LoginPage(Base):
    url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    driver = webdriver.Chrome(executable_path="Drivers/chromedriver")
    elementsDict = xmlParser.XMLParse.parseXML('LoginPage.xml')

    def login(self,username,password):
        self.driver.get(self.url)
        self.driver.find_element_by_id(self.elementsDict['tb_email_id']).clear()
        self.driver.find_element_by_id(self.elementsDict['tb_email_id']).send_keys(username)
        self.driver.find_element_by_id(self.elementsDict['tb_password_id']).clear()
        self.driver.find_element_by_id(self.elementsDict['tb_password_id']).send_keys(password)
        self.driver.find_element_by_xpath(self.elementsDict['btn_login_xpath']).click()
        self.driver.quit()
        title = self.driver.title()

        if title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False




