from Utilities.lib import SeleniumWrapper
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class CreateAccount:
    txt_fname = ("id","fullname")
    txt_email = ("id","email")
    txt_contact = ("id","contactno")
    txt_password = ("id","password")
    txt_conpassword = ("id","confirmpassword")
    btn_signup = ("name","submit")

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def CreateAcc(self,fullname,email,contactno,confirmpassword,submit):
        self.wrapper.enter_text(self.txt_fname,value="fullname")
        self.wrapper.enter_text(self.txt_email,value="email")
        # self.wrapper.page_up(self.txt_contact,value="contactno")
        # sleep(2)
        self.wrapper.enter_text(self.txt_contact,value="contactno")
        self.wrapper.enter_text(self.txt_conpassword,value="confirmpassword")
        self.wrapper.click_element(self.btn_signup)


