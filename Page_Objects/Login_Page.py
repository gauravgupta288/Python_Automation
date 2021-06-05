from Page_Objects import Base_Page
from Page_Objects.Base_Page import Base


class LoginPage(Base):
    tb_email_id = "Email"
    tb_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"

    def login(self,username,password):
        self.driver.find_element_by_id(self.tb_email_id).clear()
        self.driver.find_element_by_id(self.tb_email_id).submit(username)
        self.driver.find_element_by_id(self.tb_password_id).clear()
        self.driver.find_element_by_id(self.tb_password_id).submit(password)
        self.driver.find_element_by_xpath(self.tb_password_id).click()
        self.title = self.driver.title()
        if self.title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False



