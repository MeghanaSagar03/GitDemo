from Utilities.lib import SeleniumWrapper
from selenium.common.exceptions import NoSuchElementException
# from Utilities.excel_lib import read_headers,read_locators,attach_elements
from time import sleep

class LoginPage:
    click_login = ("link text","Login")
    txt_email = ("name", "email")
    txt_password = ("id","exampleInputPassword1")
    btn_login = ("link text", "Login")

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def login(self, email, password):
        self.wrapper.click_element(self.click_login)
        self.wrapper.enter_text(self.txt_email, value=email)
        self.wrapper.enter_text(self.txt_password, value=password)
        self.wrapper.page_down()
        sleep(2)
        self.wrapper.click_element(self.btn_login)

    def is_user_logged_in(self, email):
        _xpath = f"//a[text()='{email}']"  # dynamic xpath
        for _ in range(5):
            try:
                self.driver.find_element("xpath", _xpath).is_displayed()
                return True
            except NoSuchElementException:
                sleep(2)
                continue
        return False




























# @attach_element(LoginPage):
# class LoginPage:
#     def __init__(self,driver):
#         self.driver = driver
#         self.wrapper = SeleniumWrapper(self.driver)
#
#     def login(self, email, password):
#         self.wrapper.enter_text(self.txt_email, value=email)
#         self.wrapper.enter_text(self.txt_password, value=password)
#         self.wrapper.click_element(self.btn_login)
#
#     def is_user_logged_in(self, email):
#         _xpath = f"//a[text()='{email}']"  # dynamic xpath
#         for _ in range(5):
#             try:
#                 self.driver.find_element("xpath", _xpath).is_displayed()
#                 return True
#             except NoSuchElementException:
#                 sleep(2)
#                 continue
#         return False
