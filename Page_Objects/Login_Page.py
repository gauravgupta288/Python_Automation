from Page_Objects.Base_Page import Base
from selenium import webdriver
from Resources.xmlParser import XMLParse
from Resources.ReadProperties import ReadConfig
from datetime import datetime
from Utilities.LogGenerator import LogGen


class LoginPage(Base):
    logger = LogGen.loggen()
    driver = webdriver.Chrome(executable_path="Drivers/chromedriver")
    elementsDict = XMLParse.parseXML('LoginPage.xml')
    # Get config details
    url = ReadConfig.getUrl()
    username = ReadConfig.getAppUsername()
    password = ReadConfig.getAppPassword()

    def login(self):
        self.logger.info("############ Login Test ############")
        self.driver.get(self.url)
        self.logger.info("URL Hit")
        self.driver.find_element_by_id(self.elementsDict['tb_email_id']).clear()
        self.driver.find_element_by_id(self.elementsDict['tb_email_id']).send_keys(self.username)
        self.driver.find_element_by_id(self.elementsDict['tb_password_id']).clear()
        self.driver.find_element_by_id(self.elementsDict['tb_password_id']).send_keys(self.password)
        self.driver.find_element_by_xpath(self.elementsDict['btn_login_xpath']).click()
        title = self.driver.title
        # Validate title of home page
        if title == "Dashboard / nopCommerce administration":
            self.logger.info("Home page title is matche, test case Passed")
            assert True
        else:
            self.logger.error("Test case Failed")
            time = str(datetime.now())
            self.driver.save_screenshot("Screenshots/LoginPage_"+time+".png")
            assert False
        self.driver.quit()



